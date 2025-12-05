FROM ubuntu:25.04

RUN apt update && apt upgrade -y

# Install Debian build deps
RUN apt install -y \
    build-essential \
    devscripts \
    debhelper \
    decopy \
    dh-cargo

# Install general build deps
RUN apt install -y \
    build-essential \
    cmake \
    cmake-extras \
    curl \
    gawk \
    gettext \
    gir1.2-graphene-1.0 \
    git \
    glslang-tools \
    gobject-introspection \
    golang \
    hwdata \
    jq \
    libavcodec-dev \
    libavformat-dev \
    libavutil-dev \
    libcairo2-dev \
    libdeflate-dev \
    libdisplay-info-dev \
    libdrm-dev \
    libegl1-mesa-dev \
    libgbm-dev \
    libgdk-pixbuf-2.0-dev \
    libgdk-pixbuf2.0-bin \
    libgirepository1.0-dev \
    libgl1-mesa-dev \
    libgraphene-1.0-0 \
    libgraphene-1.0-dev \
    libgtk-3-dev \
    libgulkan-dev \
    libinih-dev \
    libinput-dev \
    libjbig-dev \
    liblerc-dev \
    libliftoff-dev \
    liblzma-dev \
    libnotify-bin \
    libpam0g-dev \
    libpango1.0-dev \
    libpipewire-0.3-dev \
    libqt6svg6 \
    libseat-dev \
    libstartup-notification0-dev \
    libswresample-dev \
    libsystemd-dev \
    libtiff-dev \
    libtiffxx6 \
    libtomlplusplus-dev \
    libudev-dev \
    libvkfft-dev \
    libvulkan-dev \
    libvulkan-volk-dev \
    libwayland-dev \
    libwebp-dev \
    libxcb-composite0-dev \
    libxcb-cursor-dev \
    libxcb-dri3-dev \
    libxcb-ewmh-dev \
    libxcb-icccm4-dev \
    libxcb-present-dev \
    libxcb-render-util0-dev \
    libxcb-res0-dev \
    libxcb-util-dev \
    libxcb-xinerama0-dev \
    libxcb-xinput-dev \
    libxcb-xkb-dev \
    libxkbcommon-dev \
    libxkbcommon-x11-dev \
    libxkbregistry-dev \
    libxml2-dev \
    libxxhash-dev \
    make \
    meson \
    ninja-build \
    openssl \
    psmisc \
    python3-mako \
    python3-markdown \
    python3-markupsafe \
    python3-yaml \
    python3-pyquery \
    qt6-base-dev \
    scdoc \
    seatd \
    spirv-tools \
    vulkan-validationlayers \
    wayland-protocols \
    xdg-desktop-portal \
    xwayland
    # libjpeg-dev \
    # libjpeg62-dev

# Install hypridle deps
RUN apt install -y \
    libsdbus-c++-dev

# Install hyprlock deps
RUN apt install -y \
    libmagic-dev

# Install hyprcursor deps
RUN apt install -y \
    libzip-dev \
    librsvg2-dev

# Install swww deps
RUN apt install -y \
    cargo \
    liblz4-dev \
    rustc

# Install wallust deps
RUN apt install -y \
    librust-jpeg-decoder-dev \
    cargo

# Install ags deps
RUN apt install -y \
    node-typescript \
    npm \
    libgjs-dev \
    gjs \
    libgtk-layer-shell-dev \
    libgtk-3-dev \
    libpulse-dev \
    libdbusmenu-gtk3-dev \
    libsoup-3.0-dev

# Install swappy deps
RUN apt install -y \
    liblocale-msgfmt-perl \
    libgtk-3-dev

# Install rofi-wayland deps
RUN apt install -y \
    bison \
    flex \
    pandoc \
    doxygen \
    cppcheck \
    ohcount \
    libmpdclient-dev \
    libnl-3-dev \
    libasound2-dev

# Install gtk-themes deps
RUN apt install -y \
    unzip \
    gtk2-engines-murrine
