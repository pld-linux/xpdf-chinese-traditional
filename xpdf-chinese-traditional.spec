Summary:	Big5 and Big5ascii encoding support for xpdf
Summary(pl):	Wsparcie kodowania Big5 i Big5ascii dla xpdf
Name:		xpdf-chinese-traditional
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}.tar.gz
URL:		http://www.foolabs.com/xpdf/
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

%description -l pl
Pakiety wspieraj±ce jêzyki Xpdf zawieraj± pliki CMap, kodowania oraz
ró¿ne inne informacje konfiguracyjne niezbêdne b±d¼ przydatne przy
okre¶lonych zestawach znaków. (Nie zawieraj± ¿adnych fontów).
Ten pakiet zawiera pliki potrzebne do u¿ywania narzêdzi Xpdf z
chiñskimi tradycyjnymi plikami PDF.

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
 if ! grep -q '-\*-fixed-medium-r-normal-\*-%s-\*-\*-\*-\*-\*-big5-0' /etc/xpdfrc; then
	echo 'displayCIDFontX	Adobe-CNS1	"-*-fixed-medium-r-normal-*-%s-*-*-*-*-*-big5-0" Big5' >> /etc/xpdfrc
 fi
 if ! grep -q '-arphic-ar pl kaitim big5-medium-r-normal--%s-\*-\*-\*-c-\*-iso10646-1' /etc/xpdfrc; then
	echo '# displayCIDFontX	Adobe-CNS1	"-arphic-ar pl kaitim big5-medium-r-normal--%s-*-*-*-c-*-iso10646-1" UCS-2' >> /etc/xpdfrc
 fi
fi

%preun
umask 022
grep -v 'Big5\.unicodeMap' /etc/xpdfrc > /etc/xpdfrc.new
grep -v 'Big5ascii\.unicodeMap' /etc/xpdfrc.new > /etc/xpdfrc
grep -v 'Adobe-CNS1\.cidToUnicode' /etc/xpdfrc > /etc/xpdfrc.new
grep -v 'CMap-chinese-traditional' /etc/xpdfrc.new > /etc/xpdfrc
grep -v '-\*-fixed-medium-r-normal-\*-%s-\*-\*-\*-\*-\*-big5-0' /etc/xpdfrc > /etc/xpdfrc.new
grep -v '-arphic-ar pl kaitim big5-medium-r-normal--%s-\*-\*-\*-c-\*-iso10646-1' /etc/xpdfrc.new > /etc/xpdfrc
rm -f /etc/xpdfrc.new

%files
%defattr(644,root,root,755)
%doc README add-to-xpdfrc
%{_datadir}/xpdf/*
