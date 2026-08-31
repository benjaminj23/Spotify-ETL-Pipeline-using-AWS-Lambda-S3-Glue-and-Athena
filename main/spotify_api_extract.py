import json
import os
from datetime import datetime

import boto3
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def lambda_handler(event, context):
    client_id = os.environ.get("client_id")
    client_secret = os.environ.get("client_secret")

    client_credentials_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )

    sp = spotipy.Spotify(
        client_credentials_manager=client_credentials_manager
    )

    playlist_link = "https://open.spotify.com/playlist/6VOedaf3eNWDOVpa9Qdlvg"
    playlist_uri = playlist_link.split("/")[-1]

    spotify_data = sp.playlist_tracks(playlist_uri)

    s3 = boto3.client("s3")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"spotify_raw_{timestamp}.json"

    s3.put_object(
        Bucket="spotifyetlprojectben",
        Key=f"raw_data/to_processed/{filename}",
        Body=json.dumps(spotify_data)
    )

    return {
        "statusCode": 200,
        "body": "Spotify data successfully extracted and stored in S3"
    }
