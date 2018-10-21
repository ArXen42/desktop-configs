-- Date: provides access to os.date with optional custom formatting
--module("vicious.widgets.sensors")

local setmetatable = setmetatable
local sensors = {}

-- {{{ Date widget type
local function worker()
f = io.popen("sensors | awk '/Core/ {print($3)}'")
cpu = ""
for line in f:lines() do
    if cpu == "" then cpu = line 
    else cpu = cpu .. "|" .. line end
end
  return "Cpu: " .. cpu 
end
-- }}}
return setmetatable(sensors, { __call = function(_, ...) return worker(...) end })