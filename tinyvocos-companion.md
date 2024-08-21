---
layout: page
title: "Tiny Vocos Companion Website"
permalink: /tinyvocos-companion
---

### TinyVOCOS Companion Website

## Abstract

Aggiungere risultati e Parte su Internet of Sounds
Neural vocoders convert time-frequency representations, such
as mel-spectrograms, into corresponding time representations.
Vocoders are essential for generative applications in audio (e.g.
text-to-speech and text-to-audio). In the Internet of Sounds
domain, generating speech signals at the edge enables the
employment of smart assistants that leverage text-to-speech
pipelines. This paper presents a scalable vocoder architecture
for small-footprint edge devices. We test the developed model
capabilities qualitatively and quantitatively on single-speaker
and multi-speaker datasets and benchmark inference speed and
memory consumption on four microcontrollers. Additionally, we
study the power consumption on an ARM Cortex-M7-powered
board. Our results demonstrate the feasibility of deploying
neural vocoders on resource-constrained edge devices, potentially
enabling new applications in IoT and edge computing scenarios
IoS and Embedded Audio scenarios. This is supported by our
best performing model achieving a MOS score of 3.95/5, while
utilizing 1.5MiB of Flash and 517KiB of ram and consuming 252
mW for a 1s audio clip inference.

## Exported Audio

### LibriTTS

<!-- <audio controls>
  <source src="{{ 'resources/tinyvocos_audio_out/tts/phinet/0.mp3' | relative_url }}" type="audio/mpeg">
  Your browser does not support the audio element.
</audio> -->
<table>

    <tr>
        <th> Reference </th>
        <th> Xinet </th>
        <th> Phinet </th>
        <th> Vocos </th>
    </tr>

<tr>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/reference/0.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/xinet/0.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/phinet/0.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/vocos/0.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
</tr>
<tr>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/reference/1.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/xinet/1.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/phinet/1.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/vocos/1.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
</tr>
<tr>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/reference/2.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/xinet/2.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/phinet/2.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/vocos/2.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
</tr>
<tr>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/reference/3.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/xinet/3.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/phinet/3.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/vocos/3.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
</tr>
<tr>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/reference/4.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/xinet/4.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/phinet/4.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/vocos/4.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
</tr>
<tr>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/reference/5.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/xinet/5.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/phinet/5.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/vocos/5.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
</tr>
<tr>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/reference/6.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/xinet/6.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/phinet/6.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/vocos/6.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
</tr>
<tr>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/reference/7.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/xinet/7.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/phinet/7.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
<td>

            <audio controls>
              <source src="{{ resources/tinyvocos_audio_out/tts/vocos/7.mp3 | url_for }}" type="audio/mpeg">
              Your browser does not support the audio element.
            </audio>
        
</td>
</tr>
</table>

### Tacotron
