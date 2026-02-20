#
# Conditional build:
%bcond_with	nondist	# with unzipped ROM files instead of xf25.zip (non-distributable package)
#
Summary:	ROM files for Atari 800 Emulator
Summary(pl.UTF-8):	Pliki ROM dla emulatora Atari 800
Name:		Atari800-rom
Version:	0
Release:	2
# xf25.zip file is distributable if ZIP contents are unmodified
# so ROMs probably can be redistributed only in original XF25 archive
%if %{with nondist}
License:	non-distributable
%else
License:	distributable without charge if unmodified (PC Xformer 2.5 license)
%endif
Group:		Applications/Emulators
Source0:	http://joy.sophics.cz/www/xf25.zip
# Source0-md5:	4dc3b6b4313e9596c4d474785a37b94d
URL:		http://www.emulators.com/xformer.htm
%if %{with nondist}
BuildRequires:	unzip
%else
Requires(post):	unzip
%endif
Conflicts:	Atari800-common < 4.2.0-1
Conflicts:	Atari800 < 1.0.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
8-bit Atari ROM files (Atari OS B, Atari XL OS, Atari Basic) for use
with Atari 800 emulator.

%if %{without nondist}
Due to license conditions, this package contains the whole PC Xformer
2.5 emulator archive.
%endif

%description -l pl.UTF-8
Pliki ROM 8-bitowego Atari (Atari OS B, Atari XL OS, Atari Basic),
przeznaczone do użycia z emulatorem Atari 800.

%if %{without nondist}
Ze względu na warunki licencji, ten pakiet zawiera całe archiwum
emulatora PC Xformer 2.5.
%endif

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/atari800

%if %{with nondist}
unzip -q -L %{SOURCE0} -d $RPM_BUILD_ROOT%{_datadir}/atari800
%{__rm} $RPM_BUILD_ROOT%{_datadir}/atari800/xf25.*
%else
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/atari800
touch $RPM_BUILD_ROOT%{_datadir}/atari800/{ataribas,atariosb,atarixl}.rom
touch $RPM_BUILD_ROOT%{_datadir}/atari800/{demos1,demos2,dos25}.xfd
touch $RPM_BUILD_ROOT%{_datadir}/atari800/mydos45d.atr
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{without nondist}
%post
cd %{_datadir}/atari800
if [ "`echo *.rom`" = "*.rom" ]; then
	umask 022
	unzip -q -L xf25.zip
	rm -f xf25.doc xf25.exe
fi
%endif

%files
%defattr(644,root,root,755)
%if %{with nondist}
%{_datadir}/atari800/ataribas.rom
%{_datadir}/atari800/atariosb.rom
%{_datadir}/atari800/atarixl.rom
%{_datadir}/atari800/demos1.xfd
%{_datadir}/atari800/demos2.xfd
%{_datadir}/atari800/dos25.xfd
%{_datadir}/atari800/mydos45d.atr
%else
%{_datadir}/atari800/xf25.zip
%ghost %{_datadir}/atari800/ataribas.rom
%ghost %{_datadir}/atari800/atariosb.rom
%ghost %{_datadir}/atari800/atarixl.rom
%ghost %{_datadir}/atari800/demos1.xfd
%ghost %{_datadir}/atari800/demos2.xfd
%ghost %{_datadir}/atari800/dos25.xfd
%ghost %{_datadir}/atari800/mydos45d.atr
%endif
