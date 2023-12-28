<CsoundSynthesizer>
<CsOptions>
-m1
-d -odac -iadc -b128 -B512
</CsOptions>
<CsInstruments>
sr = 44100
nchnls = 1
ksmps = 32
0dbfs = 1



instr 1 

    ;cues
    gkCounter init 0

    ;output to python
    chnset(gkCounter, "cue")
endin

</CsInstruments>
<CsScore>
i 1 0 360000
</CsScore>
</CsoundSynthesizer>