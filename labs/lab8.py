from lib2to3.fixer_util import p1


def magic_index(p1: list):
  for i in range(len(p1)):
    if p1[i] == i:
      return i
  return -1

def longer_than(plist: list, p2: str):
  for i in plist:
    if len(i) > len(p2):
      return i
  return ""

def num_longer_than(plist: list, p2: str):
  total = 0
  for i in plist:
    if len(i) > len(p2):
      total += 1
  return total
  return 0

def get_second_index(p1: str, p2: str) -> int:
  if p1.count(p2) > 1:
    first_index = p1.find(p2)
    second_index = p1.find(p2, first_index+1)
    return second_index
  return -1


def get_third_index(p1: str, p2: str):
    if p1.count(p2) <= 2:
      return -1
    elif p1.count(p2) > 2:
      first_index = p1.find(p2)
      second_index = p1.find(p2, first_index+1)
      third_index = p1.find(p2, second_index+1)
      return third_index


def get_domain_from_url(p1: str):
  if p1.split("//")[0] == "http:" or p1.split("//")[0] == "https:":
      p1 = p1.split("//")
      return p1[1].split("/")[0]
  elif p1.split("@")[0].split("//")[0] == "ftp:" or p1.split("@")[0] == "mailto:someone":
      p1 = p1.split("@")
      return p1[1].split("/")[0]
  return ""



