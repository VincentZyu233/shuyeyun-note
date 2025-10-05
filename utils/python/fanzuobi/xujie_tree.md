# 细节文法
 1. <句子> ::= "细节:" <左部分> "，" <右部分>

 2. <左部分> ::= "细" | <左部分> "在" <右部分> "的左边"

 3. <右部分> ::= "节" | <右部分> "在" <左部分> "的右边"

## 细节:细，节
```mermaid
graph TD
    A("句子") --> B["细节:"]
    A --> C("左部分")
    A --> D["，"]
    A --> E("右部分")
    
    C --> F["细"]
    E --> G["节"]

    class B,D,F,G leaf_node
    classDef leaf_node fill:#f9f,stroke:#333,stroke-width:2px,font-weight:bold,font-size:16px;
```

## 细节:细在节的左边，节在细的右边
```mermaid
graph TD
    A("句子") --> B["细节:"]
    A --> C("左部分")
    A --> D["，"]
    A --> E("右部分")
    
    C --> F("左部分")
    C --> G["在"]
    C --> H("右部分")
    C --> I["的左边"]
    
    F --> J["细"]
    H --> K["节"]
    
    E --> L("右部分")
    E --> M["在"]
    E --> N("左部分")
    E --> O["的右边"]
    
    L --> P["节"]
    N --> Q["细"]

    class B,D,G,I,J,K,M,O,P,Q leaf_node
    classDef leaf_node fill:#f9f,stroke:#333,stroke-width:2px,font-weight:bold,font-size:16px;
```

## 细节:细在节的左边在节在细的右边的左边，节在细的右边在细在节的左边的右边
```mermaid
graph TD
    A("句子") --> B["细节:"]
    A --> C("左部分")
    A --> D["，"]
    A --> E("右部分")

    C --> F("左部分")
    C --> G["在"]
    C --> H("右部分")
    C --> I["的左边"]
    
    F --> J("左部分")
    F --> K["在"]
    F --> L("右部分")
    F --> M["的左边"]
    
    H --> N("右部分")
    H --> O["在"]
    H --> P("左部分")
    H --> Q["的右边"]
    
    J --> R["细"]
    L --> S["节"]
    N --> T["节"]
    P --> U["细"]

    E --> V("右部分")
    E --> W["在"]
    E --> X("左部分")
    E --> Y["的右边"]
    
    V --> Z("右部分")
    V --> AA["在"]
    V --> AB("左部分")
    V --> AC["的右边"]

    X --> AD("左部分")
    X --> AE["在"]
    X --> AF("右部分")
    X --> AG["的左边"]
    
    Z --> AH["节"]
    AB --> AI["细"]
    AD --> AJ["细"]
    AF --> AK["节"]

    class B,D,G,I,K,M,O,Q,R,S,T,U,W,Y,AA,AC,AE,AG,AH,AI,AJ,AK leaf_node
    classDef leaf_node fill:#f9f,stroke:#333,stroke-width:2px,font-weight:bold,font-size:16px;
```

## 细节:细在节的左边在节在细的右边的左边在节在细的右边在细在节的左边的右边的左边，节在细的右边在细在节的左边的右边在细在节的左边在节在细的右边的左边的右边
```mermaid
graph TD
    A("句子") --> B["细节:"]
    A --> C("左部分")
    A --> D["，"]
    A --> E("右部分")

    %% ===== 左半部分 =====
    C --> F("左部分")
    C --> G["在"]
    C --> H("右部分")
    C --> I["的左边"]

    F --> J("左部分")
    F --> K["在"]
    F --> L("右部分")
    F --> M["的左边"]

    J --> N("左部分")
    J --> O["在"]
    J --> P("右部分")
    J --> Q["的左边"]

    N --> R["细"]
    P --> S["节"]

    L --> T("右部分")
    L --> U["在"]
    L --> V("左部分")
    L --> W["的右边"]

    T --> X["节"]
    V --> Y["细"]

    H --> Z("右部分")
    H --> AA["在"]
    H --> AB("左部分")
    H --> AC["的右边"]

    Z --> AD["节"]
    AB --> AE["细"]

    P --> AF("左部分")
    P --> AG["在"]
    P --> AH("右部分")
    P --> AI["的左边"]

    AF --> AJ["细"]
    AH --> AK["节"]

    %% ===== 右半部分 =====
    E --> BA("右部分")
    E --> BB["在"]
    E --> BC("左部分")
    E --> BD["的右边"]

    BA --> BE("右部分")
    BA --> BF["在"]
    BA --> BG("左部分")
    BA --> BH["的右边"]

    BE --> BI("右部分")
    BE --> BJ["在"]
    BE --> BK("左部分")
    BE --> BL["的右边"]

    BI --> BM["节"]
    BK --> BN["细"]

    BG --> BO("左部分")
    BG --> BP["在"]
    BG --> BQ("右部分")
    BG --> BR["的左边"]

    BO --> BS["细"]
    BQ --> BT["节"]

    BC --> BU("左部分")
    BC --> BV["在"]
    BC --> BW("右部分")
    BC --> BX["的左边"]

    BU --> BY["细"]
    BW --> BZ["节"]

    %% 右半部分的嵌套
    BK --> CA("左部分")
    BK --> CB["在"]
    BK --> CC("右部分")
    BK --> CD["的左边"]

    CA --> CE["细"]
    CC --> CF["节"]

    class B,D,G,I,K,M,O,Q,U,W,AA,AC,AG,AI,BB,BD,BF,BH,BJ,BL,BP,BR,BV,BX,CB,CD,R,S,X,Y,AD,AE,AJ,AK,BM,BN,BS,BT,BY,BZ,CE,CF leaf_node
    classDef leaf_node fill:#f9f,stroke:#333,stroke-width:2px,font-weight:bold,font-size:16px;

```