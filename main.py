def name():
    pdb_id=input('enter pdb code\n')
    chain = input('enter chain\n')
    return pdb_id, chain

if __name__ == '__main__':
   pdb_id, chain = name()
