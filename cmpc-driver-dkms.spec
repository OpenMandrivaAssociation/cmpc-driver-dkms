Name:			cmpc-driver-dkms
Version:		0.1.1
Release:		%mkrel 2

Summary:        Driver for Classmate PC
License:        GPLv2+
Group:          System/Kernel and hardware 
URL:            None
Source:	classmate_laptop-%{version}.tar.gz
buildarch:	noarch
Requires:       dkms kernel-desktop-devel make
Requires(post):	dkms
Provides:       classmate-laptop
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This is fixed Classmate PC driver for 4th generation too.
Use with dkms.

%prep
%setup -q -n classmate_laptop-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/src/classmate_laptop-%{version}/
cp -f * %{buildroot}/usr/src/classmate_laptop-%{version}/

%files
%defattr(-,root,root,-)
/usr/src/classmate_laptop-%{version}/*

%post
/usr/sbin/dkms add -m classmate_laptop -v %{version}
/usr/sbin/dkms build -m classmate_laptop -v %{version}
/usr/sbin/dkms install -m classmate_laptop -v %{version}

%preun
/usr/sbin/dkms remove -m classmate_laptop -v %{version} --all
