Summary:	Big5 and Big5ascii encoding support for xpdf
Summary(pl.UTF-8):	Obsługa kodowań Big5 i Big5ascii dla xpdf
Name:		xpdf-chinese-traditional
Version:	20170725
Release:	1
License:	GPL v2 or GPL v3
Group:		X11/Applications
#Source0Download: http://www.xpdfreader.com/download.html
Source0:	https://xpdfreader-dl.s3.amazonaws.com/%{name}.tar.gz
# Source0-md5:	b98832f2ca8749910381e981f481142c
URL:		http://www.xpdfreader.com/
Requires(post,preun):	grep
Requires(post,preun):	xpdf
Requires(preun):	fileutils
Requires:	xpdf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xpdf language support packages include CMap files, text encodings,
and various other configuration information necessary or useful for
specific character sets. (They do not include any fonts.)
This package provides support files needed to use the Xpdf tools with
Chinese-traditional PDF files.

%description -l pl.UTF-8
Pakiety wspierające języki Xpdf zawierają pliki CMap, kodowania oraz
różne inne informacje konfiguracyjne niezbędne bądź przydatne przy
określonych zestawach znaków (nie zawierają żadnych fontów).
Ten pakiet zawiera pliki potrzebne do używania narzędzi Xpdf z
chińskimi tradycyjnymi plikami PDF.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xpdf/CMap-chinese-traditional

install *.unicodeMap $RPM_BUILD_ROOT%{_datadir}/xpdf
install *.cidToUnicode $RPM_BUILD_ROOT%{_datadir}/xpdf
install CMap/* $RPM_BUILD_ROOT%{_datadir}/xpdf/CMap-chinese-traditional

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if [ ! -f /etc/xpdfrc ]; then
	echo 'unicodeMap	Big5		/usr/share/xpdf/Big5.unicodeMap' >> /etc/xpdfrc
	echo 'unicodeMap	Big5ascii	/usr/share/xpdf/Big5ascii.unicodeMap' >> /etc/xpdfrc
	echo 'cidToUnicode	Adobe-CNS1	/usr/share/xpdf/Adobe-CNS1.cidToUnicode' >> /etc/xpdfrc
	echo 'cMapDir		Adobe-CNS1	/usr/share/xpdf/CMap-chinese-traditional' >> /etc/xpdfrc
	echo 'toUnicodeDir			/usr/share/xpdf/CMap-chinese-traditional' >> /etc/xpdfrc
	echo 'displayCIDFontX	Adobe-CNS1	"-*-fixed-medium-r-normal-*-%s-*-*-*-*-*-big5-0" Big5' >> /etc/xpdfrc
	echo '# displayCIDFontX	Adobe-CNS1	"-arphic-ar pl kaitim big5-medium-r-normal--%s-*-*-*-c-*-iso10646-1" UCS-2' >> /etc/xpdfrc
else
 if ! grep -q 'Big5\.unicodeMap' /etc/xpdfrc; then
	echo 'unicodeMap	Big5		/usr/share/xpdf/Big5.unicodeMap' >> /etc/xpdfrc
 fi
 if ! grep -q 'Big5ascii\.unicodeMap' /etc/xpdfrc; then
	echo 'unicodeMap	Big5ascii	/usr/share/xpdf/Big5ascii.unicodeMap' >> /etc/xpdfrc
 fi
 if ! grep -q 'Adobe-CNS1\.cidToUnicode' /etc/xpdfrc; then
	echo 'cidToUnicode	Adobe-CNS1	/usr/share/xpdf/Adobe-CNS1.cidToUnicode' >> /etc/xpdfrc
 fi
 if ! grep -q 'CMap-chinese-traditional' /etc/xpdfrc; then
	echo 'cMapDir		Adobe-CNS1	/usr/share/xpdf/CMap-chinese-traditional' >> /etc/xpdfrc
	echo 'toUnicodeDir			/usr/share/xpdf/CMap-chinese-traditional' >> /etc/xpdfrc
 fi
 if ! grep -q -e '-\*-fixed-medium-r-normal-\*-%s-\*-\*-\*-\*-\*-big5-0' /etc/xpdfrc; then
	echo 'displayCIDFontX	Adobe-CNS1	"-*-fixed-medium-r-normal-*-%s-*-*-*-*-*-big5-0" Big5' >> /etc/xpdfrc
 fi
 if ! grep -q -e '-arphic-ar pl kaitim big5-medium-r-normal--%s-\*-\*-\*-c-\*-iso10646-1' /etc/xpdfrc; then
	echo '# displayCIDFontX	Adobe-CNS1	"-arphic-ar pl kaitim big5-medium-r-normal--%s-*-*-*-c-*-iso10646-1" UCS-2' >> /etc/xpdfrc
 fi
fi

%preun
if [ "$1" = "0" ]; then
	umask 022
	grep -v 'Big5\.unicodeMap' /etc/xpdfrc > /etc/xpdfrc.new
	grep -v 'Big5ascii\.unicodeMap' /etc/xpdfrc.new > /etc/xpdfrc
	grep -v 'Adobe-CNS1\.cidToUnicode' /etc/xpdfrc > /etc/xpdfrc.new
	grep -v 'CMap-chinese-traditional' /etc/xpdfrc.new > /etc/xpdfrc
	grep -v -e '-\*-fixed-medium-r-normal-\*-%s-\*-\*-\*-\*-\*-big5-0' /etc/xpdfrc > /etc/xpdfrc.new
	grep -v -e '-arphic-ar pl kaitim big5-medium-r-normal--%s-\*-\*-\*-c-\*-iso10646-1' /etc/xpdfrc.new > /etc/xpdfrc
	rm -f /etc/xpdfrc.new
fi

%files
%defattr(644,root,root,755)
%doc README add-to-xpdfrc
%{_datadir}/xpdf/Big5.unicodeMap
%{_datadir}/xpdf/Big5ascii.unicodeMap
%{_datadir}/xpdf/Adobe-CNS1.cidToUnicode
%{_datadir}/xpdf/CMap-chinese-traditional
