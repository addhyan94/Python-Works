from pytube import YouTube

YouTube('https://youtu.be/dJXCE6J1Tzo?si=WsLx7LkDY-tjyAyP').streams.first().download()