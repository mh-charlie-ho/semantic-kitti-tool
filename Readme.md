## Env
```
conda create -n kittiTool python=3.12.3
conda activate kittiTool
```

### Ground Filter Remover
You cannot remove the unlabelled points. This module removes the points according to the specified points label. So before doing this, we need to remap the similar ground point to the ground point, which is [40: "road", 48: "sidewalk", 49: "other-ground", 60: "lane-marking"] to 40. Then, we remove the points labeled 40. So, when the points are labeled "unlabeled", we can not remap to any id.
