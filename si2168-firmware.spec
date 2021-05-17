Summary:	Firmware files for Silicon Labs Si2168 DVB-T2/T/C demodulator
Name:		si2168-firmware
Version:	0
Release:	0.1
License:	Unknown
Group:		Base
Source0:	https://palosaari.fi/linux/v4l-dvb/firmware/Si2168/Si2168-A20/32e06713b33915f674bfb2c209beaea5/dvb-demod-si2168-a20-01.fw
# NoSource0-md5:	32e06713b33915f674bfb2c209beaea5
NoSource:	0
Source1:	https://palosaari.fi/linux/v4l-dvb/firmware/Si2168/Si2168-A30/3f2bc2c63285ef9323cce8689ef8a6cb/dvb-demod-si2168-a30-01.fw
# NoSource1-md5:	3f2bc2c63285ef9323cce8689ef8a6cb
NoSource:	1
Source2:	https://palosaari.fi/linux/v4l-dvb/firmware/Si2168/Si2168-B40/4.0.25/dvb-demod-si2168-b40-01.fw
# NoSource2-md5:	c8e089c351e9834060e962356f8697b8
NoSource:	2
Source3:	https://palosaari.fi/linux/v4l-dvb/firmware/Si2168/Si2168-D60/6.0.1/dvb-demod-si2168-d60-01.fw
# NoSource3-md5:	6cb3774a5c66ed4f8b7ee3c2ce4ea933
NoSource:	3
Source4:	https://palosaari.fi/linux/v4l-dvb/firmware/Si2168/dvb-demod-si2168-01.fw
# NoSource4-md5:	87c317e0b75ad49c2f2cbf35572a8093
NoSource:	4
Source5:	https://palosaari.fi/linux/v4l-dvb/firmware/Si2168/dvb-demod-si2168-02.fw
# NoSource5-md5:	d8da7ff67cd56cd8aa4e101aea45e052
NoSource:	5
URL:		https://palosaari.fi/linux/v4l-dvb/firmware/Si2168/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firmware files for Silicon Labs Si2168 DVB-T2/T/C demodulator.

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/lib/firmware

cp -p %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/dvb-demod-si2168-*.fw
