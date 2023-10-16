import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { BehaviorSubject, Observable, ReplaySubject } from 'rxjs';

export enum FetchingServerState {
  FETCHING = 1,
  DONE = 2
}

@Injectable({
  providedIn: 'root'
})
export class DataService {

    private api_server = environment.api_server

    private _fetchingStateMessage: BehaviorSubject<FetchingServerState> = new BehaviorSubject<FetchingServerState>(FetchingServerState.DONE)
    public fetchingStateMessage: Observable<FetchingServerState> = this._fetchingStateMessage.asObservable()

    private _server_response = new ReplaySubject<any>(1);
    public server_response: Observable<any> = this._server_response.asObservable()

  constructor(private HttpClient: HttpClient) {  }

  getMessageResponse(userMessage: string): Observable<any> {
    console.log("Sending data to server");
    this._fetchingStateMessage.next(FetchingServerState.FETCHING);
    
    return this.HttpClient.post(this.api_server + '/get_response', { message: userMessage });
}


}
