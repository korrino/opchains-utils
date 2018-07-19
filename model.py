#!/usr/bin/env python

# wymagana funkcjonalnosc:
#
# listowanie wszystkich opchains wybranego modelu
# listowanie wszystkich sukcesji wybranego modelu
# wypisanie drzewa generalizacji opchains w wybranym modelu
#

from lxml import etree, objectify

class Model(object):
    def __init__(self, path):
        self.path = path
        try:
            f = open(self.path, 'r')
            self.content = f.read()
            self.model = objectify.fromstring(self.content)
            f.close()
        except Exception:
            print('Error while reading model')


    def get_successions(self):
        try:
            for Succession in self.model.Model.SuccessionList.Succession:
                yield Succession
        except AttributeError:
            print('There are no Successions in the model')

    def print_successions(self):
        try:
            for Succession in self.model.Model.SuccessionList.Succession:
                print('{} -> {}'.format(Succession.Predecessor, Succession.Successor))
        except AttributeError:
            print('There are no Successions in the model')

    def get_opchains(self):
        try:
            for OPCHAIN in self.model.Model.OpchainList.OPCHAIN:
                yield OPCHAIN
        except AttributeError:
            print('There are no OPCHAINs in the model')

    def print_opchain_short(self, OPCHAIN, prefix=''):
        print('{}{}: {}'.format(prefix, OPCHAIN.Id, OPCHAIN.Name))

    def print_tree_0(self):
        try:
            for OPCHAIN in self.model.Model.OpchainList.OPCHAIN:
                if(OPCHAIN.GeneralizationId == 0):
                    self.print_tree(OPCHAIN, '')
        except AttributeError:
            print('There are no OPCHAINs in the model')

    def print_opchain(self, id_):
        try:
            OPCHAIN = self.model.xpath('//OPCHAIN[Id={}]'.format(id_))[0]
            print('''
OPCHAIN-{}: {}:
Id: \t{}
GenId: \t{}
Name: \t{}
URL: \t{}

Description: 
{}
--
'''.format(OPCHAIN.Id, OPCHAIN.Name, OPCHAIN.Id, OPCHAIN.GeneralizationId, OPCHAIN.Name, OPCHAIN.URL, OPCHAIN.Description))
        except IndexError:
            print('Not found')
            raise IndexError
        

    def print_tree(self, parent, prefix):
        self.print_opchain_short(parent, prefix)
        for OPCHAIN in self.model.Model.OpchainList.OPCHAIN:
            if(OPCHAIN.GeneralizationId == parent.Id):
                self.print_tree(OPCHAIN, prefix+' ')

    def get_last(self):
        try:
            s = sorted(self.model.Model.OpchainList.OPCHAIN, key=lambda x: x.Id, reverse=True) 
            return s[0]
        except AttributeError:
            print('Model is empty')
            return None

    def print_last(self):
        try:
            s = sorted(self.model.Model.OpchainList.OPCHAIN, key=lambda x: x.Id, reverse=True) 
            print(s[0].Id)
        except AttributeError:
            print('Model is empty')
            return None

    def append_opchain(self, OPCHAIN):
        self.model.Model.OpchainList.append(OPCHAIN)

    def append_succession(self, Succession):
        try:
            for s in self.model.Model.SuccessionList.Succession:
                if((s.Successor == Succession.Successor) and (s.Predecessor == Successor.Predecessor)):
                    print('Already there')
                    raise AttributeError
        except Exception:
            pass

        self.model.Model.SuccessionList.append(Succession)

    def remove_opchain(self, id_):
        #print('//OPCHAIN[Id={}]'.format(id_))
        try:
            bad = self.model.xpath('//OPCHAIN[Id={}]'.format(id_))[0]
            bad.getparent().remove(bad)
        except IndexError:
            print('Not found')
            raise IndexError

    def remove_succession(self, pid, sid):
        try:
            bad = self.model.xpath('//Succession[Predecessor={} and Successor={}]'.format(pid, sid))[0]
            bad.getparent().remove(bad)
            print('Removed')
        except AttributeError:
            print('There are no Successions in the model')
        
        
    def commit(self):
        f = open(self.path, 'wb')
        f.write(etree.tostring(self.model, pretty_print = True))
        f.close()

