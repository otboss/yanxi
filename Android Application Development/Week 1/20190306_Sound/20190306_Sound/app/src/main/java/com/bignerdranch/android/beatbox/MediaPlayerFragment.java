package com.bignerdranch.android.beatbox;


import android.app.Activity;
import android.content.pm.ActivityInfo;
import android.media.MediaPlayer;
import android.net.Uri;
import android.os.Bundle;
import android.support.v4.app.DialogFragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.MediaController;
import android.widget.SeekBar;
import android.widget.VideoView;

import static com.bignerdranch.android.beatbox.SingleFragmentActivity.mMediaPlayer;


public class MediaPlayerFragment extends DialogFragment {
    VideoView videoview;
    Button dismiss;
    Button play;
    Button forward;
    Button rewind;
    SeekBar mseek;

    private int forwardTime = 5000;
    private int backwardTime = 5000;

    MediaController controls;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        final View rootView = inflater.inflate(R.layout.fragment_media_player, container, false);

        getActivity().setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_FULL_SENSOR);
        dismiss = (Button) rootView.findViewById(R.id.dismiss);
        play = (Button) rootView.findViewById(R.id.btn_play);
        forward = (Button) rootView.findViewById(R.id.btn_ff);
        rewind = (Button) rootView.findViewById(R.id.btn_rwd);
        mseek = (SeekBar) rootView.findViewById(R.id.seekBar);
        videoview = rootView.findViewById(R.id.videoView);
        String videopath = "android.resource://com.bignerdranch.android.beatbox/raw/hiphop";
        Uri uri = Uri.parse(videopath);
        videoview.setVideoURI(uri);

        controls = new MediaController(getContext());

        mseek.setClickable(false);

        dismiss.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                dismiss();
                mMediaPlayer.start();
            }
        });

        videoview.setOnPreparedListener(new MediaPlayer.OnPreparedListener() {

            @Override
            public void onPrepared(final MediaPlayer mp) {

                mp.setOnVideoSizeChangedListener(new MediaPlayer.OnVideoSizeChangedListener() {
                    @Override
                    public void onVideoSizeChanged(MediaPlayer mp, int width, int height) {
                        videoview.setMediaController(controls);
                        controls.setAnchorView(videoview);

                        ((ViewGroup) controls.getParent()).removeView(controls);
                        ((FrameLayout) rootView.findViewById(R.id.videoViewWrapper)).addView(controls);

                        controls.setVisibility(View.VISIBLE);
                    }
                });
                videoview.start();
                mseek.setMax(videoview.getDuration());
                mseek.postDelayed(onEverySecond, 1000);
            }
        });

        mseek.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {
            }

            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {
            }

            @Override
            public void onProgressChanged(SeekBar seekBar, int progress,
                                          boolean fromUser) {

                if(fromUser) {
                    // this is when actually seekbar has been seeked to a new position
                    videoview.seekTo(progress);
                }
            }
        });

        play.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(videoview.isPlaying()){
                    videoview.pause();
                    play.setBackgroundResource(R.drawable.ic_play_arrow_black_24dp);
                }else if(!videoview.isPlaying()) {
                    videoview.start();
                    play.setBackgroundResource(R.drawable.ic_pause_black_24dp);
                }
            }
        });

        forward.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                forwardSong();
            }
        });

        rewind.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                rewindSong();
            }
        });


        return rootView;
    }

    private Runnable onEverySecond=new Runnable() {
        //Tells the application to start the seekbar when activated
        @Override
        public void run() {

            if(mseek != null) {
                mseek.setProgress(videoview.getCurrentPosition());
            }

            if(videoview.isPlaying()) {
                mseek.postDelayed(onEverySecond, 1000);
            }

        }
    };

    public void forwardSong() {
        if (videoview != null) {
            int currentPosition = videoview.getCurrentPosition();
            if (currentPosition + forwardTime <= videoview.getDuration()) {
                videoview.seekTo(currentPosition + forwardTime);
            } else {
                videoview.seekTo(videoview.getDuration());
            }
        }
    }

    public void rewindSong() {
        if (videoview != null) {
            int currentPosition = videoview.getCurrentPosition();
            if (currentPosition - backwardTime >= 0) {
                videoview.seekTo(currentPosition - backwardTime);
            } else {
                videoview.seekTo(0);
            }
        }
    }

}
