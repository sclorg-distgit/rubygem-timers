%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from timers-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name timers

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 1.1.0
Release: 4%{?dist}
Summary: Pure Ruby one-shot and periodic timers
Group: Development/Languages
License: MIT
URL: https://github.com/celluloid/timers
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}rubygems
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ror}rubygem(rspec)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
Schedule procs to run after a certain time using any API that accepts a timeout

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Remove unecessary files
rm %{buildroot}%{gem_instdir}/{Rakefile,Gemfile,%{gem_name}.gemspec,.travis.yml,.gitignore,.rspec}

%check
pushd .%{gem_instdir}

# Bundler is used only for development. No need to install it.
sed -i '/bundler/d' spec/spec_helper.rb
sed -i '/[Cc]overalls/d' spec/spec_helper.rb

%{?scl:scl enable %{scl} - << \EOF}
rspec spec/
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGES.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec/

%changelog
* Thu Oct 16 2014 Josef Stribny <jstribny@redhat.com> - 1.1.0-4
- Add SCL macros

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 03 2013 Axilleas Pipinellis <axilleas@axilleas.me> - 1.1.0-2
- Fix Summary/Description tags

* Thu May 30 2013 Axilleas Pipinellis <axilleas@axilleas.me> - 1.1.0-1
- Initial package
