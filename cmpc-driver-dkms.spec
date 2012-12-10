Name:			cmpc-driver-dkms
Version:		0.1.1
Release:		%mkrel 3

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
/usr/sbin/dkms --rpm_safe_upgrade add -m classmate_laptop -v %{version}
/usr/sbin/dkms --rpm_safe_upgrade build -m classmate_laptop -v %{version}
/usr/sbin/dkms --rpm_safe_upgrade install -m classmate_laptop -v %{version} --force

# rmmod any old driver if present and not in use (e.g. by X)
rmmod classmate_laptop > /dev/null 2>&1 || true

%preun
/usr/sbin/dkms --rpm_safe_upgrade remove -m classmate_laptop -v %{version} --all

# rmmod any old driver if present and not in use (e.g. by X)
rmmod classmate_laptop > /dev/null 2>&1 || true


%changelog
* Sat Dec 10 2011 Александр Казанцев <kazancas@mandriva.org> 0.1.1-3mdv2012.0
+ Revision: 740039
- fix dkms add and remove for safetly update

* Wed Dec 07 2011 Александр Казанцев <kazancas@mandriva.org> 0.1.1-2
+ Revision: 738559
- imported package cmpc-driver-dkms

