name=nagios-plugins-voms
spec=spec/$(name).spec
version=$(shell grep "Version:" $(spec) | sed -e "s/Version://g" -e "s/[ \t]*//g")
release=1
rpmbuild_dir=$(shell pwd)/rpmbuild

all: clean	rpm

clean:	
		rm -rf $(rpmbuild_dir) tgz RPMS

rpm:	
		mkdir -p	$(rpmbuild_dir)/BUILD $(rpmbuild_dir)/RPMS \
					$(rpmbuild_dir)/SOURCES $(rpmbuild_dir)/SPECS \
					$(rpmbuild_dir)/SRPMS

		tar -cvzf $(rpmbuild_dir)/SOURCES/$(name)-$(version).tar.gz Makefile src/* spec/* README.md
		rpmbuild --nodeps -v -ba $(spec) --define "_topdir $(rpmbuild_dir)" 

etics:	dist rpm
		mkdir -p tgz RPMS
		cp target/*.tar.gz tgz
		cp -r $(rpmbuild_dir)/RPMS/* $(rpmbuild_dir)/SRPMS/* RPMS
