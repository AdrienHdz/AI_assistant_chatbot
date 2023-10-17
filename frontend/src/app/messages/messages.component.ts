import { AfterViewInit, Component, ElementRef, Renderer2, ViewChild } from '@angular/core';
import { FormControl, Validators, FormGroup } from '@angular/forms';
import { DataService, FetchingServerState } from '../service/dataservice.service';
import { Observable, Subscription } from 'rxjs';

interface Message {
  text: string;
  user: string;
  avatar: string;
  bgClass: string;
  textColor: string;
}

@Component({
  selector: 'app-messages',
  templateUrl: './messages.component.html',
  styleUrls: ['./messages.component.css']
})
export class MessagesComponent implements AfterViewInit {
  userMessages: Message[] = [];
  userMessageControl = new FormControl('', [Validators.required, Validators.minLength(1)]);
  uploadForm = new FormGroup({
    userMessage: this.userMessageControl
  });

  showSpinner: boolean = false;
  private subs = new Subscription();

  @ViewChild('loopVideo') loopVideo!: ElementRef<HTMLVideoElement>;
  @ViewChild('secondVideo') secondVideo!: ElementRef<HTMLVideoElement>;
  @ViewChild('messageContainer') messageContainer!: ElementRef;

  constructor(
    private dataService: DataService,
    private renderer: Renderer2
  ) {
    this.subs.add(
      this.dataService.fetchingStateMessage.subscribe(state => {
        this.showSpinner = state === FetchingServerState.FETCHING;
      })
    )
  }

  onSubmit(event: Event) {
    event.preventDefault();
    const userMessage = this.uploadForm.value.userMessage;
    if (userMessage) {
        this.addUserMessage(userMessage);
        this.uploadForm.controls['userMessage'].setValue('')
        this.dataService.getMessageResponse(userMessage)
            .subscribe(response => {
                this.addServerMessage(response.script_response);
                this.setVideoSourceAndPlay(response.url_response);
                console.log(response)
                this.dataService.currentSessionId = response.session_id;
                this.setFetchingStateDone();  
            }, error => {
                console.error('Error fetching server response:', error);
                this.setFetchingStateDone();  
            });
      }
  }

  setFetchingStateDone() {
      (this.dataService as any)._fetchingStateMessage.next(FetchingServerState.DONE);
  }

  addServerMessage(text: string) {
    const serverMsg: Message = {
      text: text,
      user: 'Server',
      avatar: '../../assets/avatar_profile_pic.png',
      bgClass: 'bg-white',
      textColor: 'text-slate-800'
    };
    this.userMessages.push(serverMsg);
    setTimeout(() => {
      this.scrollToBottom();
    });
  }

  addUserMessage(text: string) {
    const userMsg: Message = {
      text: text,
      user: 'Current User',
      avatar: '../../assets/photo_profil.jpeg',
      bgClass: 'bg-indigo-500',
      textColor: '#FFFFFF'
    };
    this.userMessages.push(userMsg);
    setTimeout(() => {
      this.scrollToBottom();
    });
  }

  ngAfterViewInit() {
    this.renderer.setProperty(this.loopVideo.nativeElement, 'muted', true);
    this.playLoopVideo();
    this.renderer.setStyle(this.secondVideo.nativeElement, 'display', 'none');
  }

  playLoopVideo() {
    this.renderer.setStyle(this.loopVideo.nativeElement, 'display', 'block');
    this.loopVideo.nativeElement.play();
  }

  playSecondVideo() {
    this.renderer.setStyle(this.loopVideo.nativeElement, 'display', 'none');
    this.renderer.setStyle(this.secondVideo.nativeElement, 'display', 'block');
    this.secondVideo.nativeElement.play();
  }

  onSecondVideoEnded() {
    this.setRandomLoopVideoSource();
    this.renderer.setStyle(this.secondVideo.nativeElement, 'display', 'none'); 
    this.playLoopVideo();
  }

  setVideoSourceAndPlay(url: string) {
    this.renderer.setAttribute(this.secondVideo.nativeElement, 'src', url);
    this.playSecondVideo();
  }

  setRandomLoopVideoSource() {
    const videoOptions = [
      '../assets/waiting_avatar.mp4',
      '../assets/waiting_avatar2.mp4',
      '../assets/waiting_avatar3.mp4'
    ];
    const randomIndex = Math.floor(Math.random() * videoOptions.length);
    const selectedVideo = videoOptions[randomIndex];
    const loopVideoSource = this.renderer.selectRootElement('#loopVideoSource');
    this.renderer.setAttribute(loopVideoSource, 'src', selectedVideo);
    this.loopVideo.nativeElement.load();
  }

  scrollToBottom(): void {
    try {
      this.messageContainer.nativeElement.scrollTop = this.messageContainer.nativeElement.scrollHeight;
    } catch (err) { }
  }

  ngOnDestroy() {
    this.subs.unsubscribe();
  }
}
