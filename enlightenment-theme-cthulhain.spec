%define	_theme	cthulhain
Summary:	Theme based on the fluxbox theme Cthulhain
Name:		enlightenment-theme-%{_theme}
Version:	0.3
%define		_pre pre2
Release:	0.%{_pre}.1
License:	GPL
Group:		Themes
Source0:	http://www.get-e.org/Themes/E17/_files/%{_theme}-%{version}%{_pre}.edj
# Source0-md5:	1ab3c816e9d607118371bcb9d30e9433
URL:		http://www.get-e.org/Themes/E17/
Requires:	enlightenmentDR17
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Theme that's based on the fluxbox theme Cthulhain.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/enlightenmentDR17/data/themes

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/enlightenmentDR17/data/themes/%{_theme}.edj

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/enlightenmentDR17/data/themes/%{_theme}.edj
