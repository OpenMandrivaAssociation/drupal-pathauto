%define modname		pathauto
%define drupal_version	7
%define module_version	1.1
%define version		%{drupal_version}.x.%{module_version}
%define tarname		%{modname}-%{drupal_version}.x-%{module_version}

Name:		drupal-%{modname}
Summary:	Pathauto module for Drupal
Version:	%{version}
Release:	1
License:	GPLv2+
Group:		Networking/WWW
URL:		https://drupal.org/project/%{modname}
Source0:	http://ftp.drupal.org/files/projects/%{tarname}.tar.gz
Requires:	drupal >= %{drupal_version}
Requires:	drupal < %{lua: print(rpm.expand("%{drupal_version}")+1)}
BuildArch:	noarch

%description
The Pathauto module automatically generates URL/path aliases for various kinds
of content (nodes, taxonomy terms, users) without requiring the user
to manually specify the path alias. This allows you to have URL aliases like
/category/my-node-title instead of /node/123. The aliases are based
upon a "pattern" system that uses tokens which the administrator can change.

%prep
%setup -q -n %{modname}

%build

%install
%__install -d -m 0755 %{buildroot}%{_var}/www/drupal/modules/
cp -a . %{buildroot}%{_var}/www/drupal/modules/%{modname}
rm -f %{buildroot}%{_var}/www/drupal/modules/%{modname}/*.txt

%files
%{_var}/www/drupal/modules/%{modname}
%doc API.txt README.txt
