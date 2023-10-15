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
  readonly sampleMessages: Message[] = [
    {
      text: 'Can anyone help? I have a question about Acme Professional',
      user: 'User 01',
      avatar: '../../assets/avatar_profile_pic.png',
      bgClass: 'bg-white',
      textColor: 'text-slate-800'
    },
    {
      text: 'Hey Dominik Lamakani 👋<br />Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 🙌',
      user: 'User 02',
      avatar: '../../assets/photo_profil.jpeg',
      bgClass: 'bg-indigo-500',
      textColor: '#ffffff'
    }
  ];

  userMessages: Message[] = [];
  userMessageControl = new FormControl('', [Validators.required, Validators.minLength(1)]);
  uploadForm = new FormGroup({
    userMessage: this.userMessageControl
  });

  showSpinner: boolean = false;
  private subs = new Subscription();

  @ViewChild('loopVideo') loopVideo!: ElementRef<HTMLVideoElement>;
  @ViewChild('secondVideo') secondVideo!: ElementRef<HTMLVideoElement>;

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
      this.dataService.getMessageResponse(userMessage);
    }
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
    this.playLoopVideo();
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

  ngOnDestroy() {
    this.subs.unsubscribe();
  }
}
