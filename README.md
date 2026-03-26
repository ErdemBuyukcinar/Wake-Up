#  Personal Voice Assistant 🤖

A lightweight, customizable Python-based voice assistant inspired by Tony Stark's J.A.R.V.I.S.(and from the famous scene from Iron Man 2). This script listens for specific voice commands to automatically set up your digital workspace by launching web pages, opening code editors, and running desktop applications.

## ✨ Features
* **Voice Recognition:** Uses Google's Speech Recognition API to understand English voice commands.
* **Text-to-Speech (TTS):** Provides audible feedback and status updates using your system's native voices.
* **Workspace Automation:** Opens specific media URLs, launches Visual Studio Code with a pre-defined project, and starts desktop AI assistants (like Claude) simultaneously.
* **Standby Mode:** Continuously listens in the background until the wake word is detected or the shutdown command is given.

## 🛠️ Prerequisites
Before running the script, ensure you have Python installed on your system. You will also need to install the following required libraries:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
```

##TR
# Kişisel Sesli Asistan 🤖

Tony Stark'ın J.A.R.V.I.S.'inden (ve Iron Man 2'de bulunan o meşhur sahneden) ilham alan, hafif ve özelleştirilebilir Python tabanlı bir sesli asistan. Bu komut dosyası, web sayfalarını başlatarak, kod editörlerini açarak ve masaüstü uygulamalarını çalıştırarak dijital çalışma alanınızı otomatik olarak kurmak için belirli sesli komutları dinler.

## ✨ Özellikler
* **Ses Tanıma:** İngilizce sesli komutları anlamak için Google'ın Konuşma Tanıma API'sini kullanır.

* **Metinden Sese (TTS):** Sisteminizin yerel seslerini kullanarak sesli geri bildirim ve durum güncellemeleri sağlar.

* **Çalışma Alanı Otomasyonu:** Belirli medya URL'lerini açar, önceden tanımlanmış bir projeyle Visual Studio Code'u başlatır ve masaüstü yapay zeka asistanlarını (Claude gibi) eş zamanlı olarak başlatır.

* **Bekleme Modu:** Uyandırma kelimesi algılanana veya kapatma komutu verilene kadar arka planda sürekli olarak dinler.

## 🛠️ Önkoşullar
Komut dosyasını çalıştırmadan önce sisteminizde Python'ın kurulu olduğundan emin olun. Ayrıca aşağıdaki gerekli kütüphaneleri de kurmanız gerekecektir:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
