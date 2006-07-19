%define	_theme	cthulhain
Summary:	Theme based on the Fluxbox theme Cthulhain
Summary(pl):	Motyw oparty na motywie Cthulhain Fluxboksa
Name:		enlightenment-theme-%{_theme}
Version:	0.3
%define		_pre pre3
Release:	0.%{_pre}.1
License:	GPL
Group:		Themes
Source0:	http://e.oceighty.net/releases/%{_theme}-%{version}%{_pre}.edj
# Source0-md5:	663ed0f7b98b27137f64b1ec23b10b55
URL:		http://www.get-e.org/Themes/E17/
Requires:	enlightenment
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Theme that's based on the Fluxbox theme Cthulhain.

%description -l pl
Motyw oparty na motywie Cthulhain Fluxboksa.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/enlightenment/data/themes

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/enlightenment/data/themes/%{_theme}.edj

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/enlightenment/data/themes/%{_theme}.edj
