---
page_id: 749
revision_id: 1021
source_url: https://second-renaissance.fandom.com/wiki/Module%3AMiddleclass
raw_sha256: e3726c688b93ce660b2207a66a538f46fa3ad880a636407cca3e82efdd1149a1
---

# Module:Middleclass

## Preserved source

```wikitext
local middleclass = {
  _VERSION     = 'middleclass v3.0.1',
  _DESCRIPTION = 'Object Orientation for Lua',
  _URL         = 'https://github.com/kikito/middleclass',
  _LICENSE     = [MIT LICENSE

    Copyright (c) 2011 Enrique García Cota

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the
    "Software"), to deal in the Software without restriction, including
    without limitation the rights to use, copy, modify, merge, publish,
    distribute, sublicense, and/or sell copies of the Software, and to
    permit persons to whom the Software is furnished to do so, subject to
    the following conditions:

    The above copyright notice and this permission notice shall be included
    in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.](https://second-renaissance.fandom.com/wiki/MIT_LICENSE

____Copyright_(c)_2011_Enrique_García_Cota

____Permission_is_hereby_granted,_free_of_charge,_to_any_person_obtaining_a
____copy_of_this_software_and_associated_documentation_files_(the
____"Software"),_to_deal_in_the_Software_without_restriction,_including
____without_limitation_the_rights_to_use,_copy,_modify,_merge,_publish,
____distribute,_sublicense,_and/or_sell_copies_of_the_Software,_and_to
____permit_persons_to_whom_the_Software_is_furnished_to_do_so,_subject_to
____the_following_conditions:

____The_above_copyright_notice_and_this_permission_notice_shall_be_included
____in_all_copies_or_substantial_portions_of_the_Software.

____THE_SOFTWARE_IS_PROVIDED_"AS_IS",_WITHOUT_WARRANTY_OF_ANY_KIND,_EXPRESS
____OR_IMPLIED,_INCLUDING_BUT_NOT_LIMITED_TO_THE_WARRANTIES_OF
____MERCHANTABILITY,_FITNESS_FOR_A_PARTICULAR_PURPOSE_AND_NONINFRINGEMENT.
____IN_NO_EVENT_SHALL_THE_AUTHORS_OR_COPYRIGHT_HOLDERS_BE_LIABLE_FOR_ANY
____CLAIM,_DAMAGES_OR_OTHER_LIABILITY,_WHETHER_IN_AN_ACTION_OF_CONTRACT,
____TORT_OR_OTHERWISE,_ARISING_FROM,_OUT_OF_OR_IN_CONNECTION_WITH_THE
____SOFTWARE_OR_THE_USE_OR_OTHER_DEALINGS_IN_THE_SOFTWARE.)
}

local function _setClassDictionariesMetatables(aClass)
  local dict = aClass.__instanceDict
  dict.__index = dict

  local super = aClass.super
  if super then
    local superStatic = super.static
    setmetatable(dict, super.__instanceDict)
    setmetatable(aClass.static, { __index = function(_,k) return dict[k] or superStatic[k] end })
  else
    setmetatable(aClass.static, { __index = function(_,k) return dict[k] end })
  end
end

local function _setClassMetatable(aClass)
  setmetatable(aClass, {
    __tostring = function() return "class " .. aClass.name end,
    __index    = aClass.static,
    __newindex = aClass.__instanceDict,
    __call     = function(self, ...) return self:new(...) end
  })
end

local function _createClass(name, super)
  local aClass = { name = name, super = super, static = {}, __mixins = {}, __instanceDict={} }
  aClass.subclasses = setmetatable({}, {__mode = "k"})

  _setClassDictionariesMetatables(aClass)
  _setClassMetatable(aClass)

  return aClass
end

local function _createLookupMetamethod(aClass, name)
  return function(...)
    local method = aClass.super[name]
    assert( type(method)=='function', tostring(aClass) .. " doesn't implement metamethod '" .. name .. "'" )
    return method(...)
  end
end

local function _setClassMetamethods(aClass)
  for _,m in ipairs(aClass.__metamethods) do
    aClass[m]= _createLookupMetamethod(aClass, m)
  end
end

local function _setDefaultInitializeMethod(aClass, super)
  aClass.initialize = function(instance, ...)
    return super.initialize(instance, ...)
  end
end

local function _includeMixin(aClass, mixin)
  assert(type(mixin)=='table', "mixin must be a table")
  for name,method in pairs(mixin) do
    if name ~= "included" and name ~= "static" then aClass[name] = method end
  end
  if mixin.static then
    for name,method in pairs(mixin.static) do
      aClass.static[name] = method
    end
  end
  if type(mixin.included)=="function" then mixin:included(aClass) end
  aClass.__mixins[mixin] = true
end

local Object = _createClass("Object", nil)

Object.static.__metamethods = { '__add', '__call', '__concat', '__div', '__ipairs', '__le',
                                '__len', '__lt', '__mod', '__mul', '__pairs', '__pow', '__sub',
                                '__tostring', '__unm'}

function Object.static:allocate()
  assert(type(self) == 'table', "Make sure that you are using 'Class:allocate' instead of 'Class.allocate'")
  return setmetatable({ class = self }, self.__instanceDict)
end

function Object.static:new(...)
  local instance = self:allocate()
  instance:initialize(...)
  return instance
end

function Object.static:subclass(name)
  assert(type(self) == 'table', "Make sure that you are using 'Class:subclass' instead of 'Class.subclass'")
  assert(type(name) == "string", "You must provide a name(string) for your class")

  local subclass = _createClass(name, self)
  _setClassMetamethods(subclass)
  _setDefaultInitializeMethod(subclass, self)
  self.subclasses[subclass] = true
  self:subclassed(subclass)

  return subclass
end

function Object.static:subclassed(other) end

function Object.static:isSubclassOf(other)
  return type(other)                   == 'table' and
         type(self)                    == 'table' and
         type(self.super)              == 'table' and
         ( self.super == other or
           type(self.super.isSubclassOf) == 'function' and
           self.super:isSubclassOf(other)
         )
end

function Object.static:include( ... )
  assert(type(self) == 'table', "Make sure you that you are using 'Class:include' instead of 'Class.include'")
  for _,mixin in ipairs({...}) do _includeMixin(self, mixin) end
  return self
end

function Object.static:includes(mixin)
  return type(mixin)          == 'table' and
         type(self)           == 'table' and
         type(self.__mixins)  == 'table' and
         ( self.__mixins[mixin] or
           type(self.super)           == 'table' and
           type(self.super.includes)  == 'function' and
           self.super:includes(mixin)
         )
end

function Object:initialize() end

function Object:__tostring() return "instance of " .. tostring(self.class) end

function Object:isInstanceOf(aClass)
  return type(self)                == 'table' and
         type(self.class)          == 'table' and
         type(aClass)              == 'table' and
         ( aClass == self.class or
           type(aClass.isSubclassOf) == 'function' and
           self.class:isSubclassOf(aClass)
         )
end



function middleclass.class(name, super, ...)
  super = super or Object
  return super:subclass(name, ...)
end

middleclass.Object = Object

setmetatable(middleclass, { __call = function(_, ...) return middleclass.class(...) end })

return middleclass
```

## Provenance

Raw source: `bronze/pages/749/1021.wikitext` · revision `1021` · [upstream](https://second-renaissance.fandom.com/wiki/Module%3AMiddleclass)
