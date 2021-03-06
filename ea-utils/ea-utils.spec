%define name ea-utils
%define ver 1.1.2
%define rel 358

Summary: 	fastq-processing utilities
Name:           %{name}
Version:        %{ver}
Release:        %{rel}
Source:         %{name}.tar.gz
Prefix:         /usr
BuildRoot:      /tmp/%{name}-%{ver}-root
Vendor:         Expression Analysis <earonesty@expressionanalysis.com>
URL:            https://code.google.com/p/ea-utils/
License: 	MIT
Group: 		Applications/Engineering
Distribution: 	Centos 5
Packager: 	Erik Aronesty <earonesty@expressionanalysis.com>

%description
Utilities for processing fastq files, stitching paired-end reads,
demultiplexing paired-end in-sync, adapter-trimming & skew removal.

%prep
%setup -c

%install
make PREFIX=%{buildroot}/%{_prefix} install

%clean
rm -rf %{buildroot}

%files

%{_bindir}/fastq-join
%{_bindir}/fastq-clipper
%{_bindir}/fastq-mcf
%{_bindir}/fastq-multx
