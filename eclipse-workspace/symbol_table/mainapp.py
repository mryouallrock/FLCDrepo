'''
Created on Oct 14, 2020

@author: Andrei
'''
from sym_tbl import Symbol_table
from hash_tbl import Hash_table

ht = Hash_table()
st = Symbol_table(ht)

st.add_symbol("name", "char")
print(st)
st.add_symbol("a", "bool")
print(st)
st.remove_symbol("name")
print(st)
print(st.look_up("a"))