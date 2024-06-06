Search String = $XR **AND** ($T **OR** $B) **AND** $S **NOT** $UX

### $XR

* XR related keywords
* Search in title
* "virtual reality" OR "augmented reality" OR "mixed reality" OR "extended reality" OR VR OR AR OR XR OR MR

### $T

* Synonyms of "testing"
* Search in title
* test OR validation OR verification

### $S

* could be removed, only for narrowing the search down
* keywords for identifing XR **software**
* search in full text
* software OR application

### $UX

* could be removed, only for narrowing the search down
* keywords related to user experience
* search in title 
* usability

### Studies for search string quality evaluation

| Title                                                        | DOI                                                          | included |
| ------------------------------------------------------------ | ------------------------------------------------------------ | :------: |
| VRTest: An Extensible Framework for Automatic Testing of Virtual Reality Scenes | [10.1145/3510454.3516870](https://doi.org/10.1145/3510454.3516870) |    T     |
| VRGuide: Efficient Testing of Virtual Reality Scenes via Dynamic Cut Coverage | [10.1109/ASE56229.2023.00197](https://doi.org/10.1109/ASE56229.2023.00197) |    T     |
| Virtual Reality (VR) Automated Testing in the Wild: A Case Study on Unity-Based VR Applications | https://doi.org/10.1145/3597926.3598134                      |    T     |
| PredART: Towards Automatic Oracle Prediction of Object Placements in Augmented Reality Testing | https://doi.org/10.1145/3551349.3561160                      |    T     |
| Automated testing of virtual reality application interfaces  | https://doi.org/10.1145/769953.769966                        |    T     |
| Automated Test of VR Applications                            | https://doi.org/10.1007/978-3-030-60703-6_18                 |    T     |
| An automated functional testing approach for virtual reality applications | https://doi.org/10.1002/stvr.1690                            |    T     |



```
# Year
2000 - 2024

# title
"virtual reality" OR "augmented reality" OR "mixed reality" OR "extended reality" OR "VR" OR "AR" OR "XR" OR "MR" 
AND 
test* OR verif* OR validat*
test OR testing OR validate OR validation OR verify OR verification

# ProQuest
title(("virtual reality" OR "augmented reality" OR "mixed reality" OR "extended reality" OR "VR" OR "AR" OR "XR" OR "MR") AND (test* OR validat* OR verif* OR bug* OR defect* OR fault* OR error*) NOT usability) AND (software OR application*)
```

```
# ScienceDirect
* Wildcards '*' are not supported
* Title can only contain 8 boolean connectors
* Use $XR in 'Title' and $T in 'Title, abstract or author-specified keywords'
```

