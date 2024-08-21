---
layout: page
title: "Tiny Vocos Companion Website"
permalink: /tinyvocos-companion
---

# Abstract

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

# Exported Audio

## LibriTTS

<audio controls>
  <source src="{{ site.baseurl }}/resources/tinyvocos_audio_out/tts/phinet/0.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

## Tacotron
