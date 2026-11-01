# Complete arithmetic specification of the triangle-monitor threshold

This appendix defines the height using natural-number arithmetic only. Every
function is given before its nonrecursive uses. Addition, multiplication, powers,
maximum, minimum, factorial and binomial coefficients have their usual meaning;
subtraction of natural numbers is truncated at zero. Pattern clauses `0` and
`n+1` define finite recursion. A `let` introduces an intermediate value.

For positive α, C and η, and integers h≥6 and q≥0, put

\[
K=\max\{2,h,q,\lceil\alpha\rceil_+,\lceil1/\alpha\rceil_+,
\lceil C\rceil_+,\lceil\eta\rceil_+,\lceil1/\eta\rceil_+\}.
\]

Let H(K,h,q) be `paperIIITriangleTowerHeight K h q` at the end of the program.
Define tow₂(0)=1 and tow₂(r+1)=2^(tow₂(r)). The order bound is
n≥tow₂(H(K,h,q)). It applies to the triangle-statistic conclusion of T+ only.
No tower bound for the simultaneous Pasch conclusion is asserted.

The definitions are printed in Lean's arithmetic syntax to avoid an ambiguous
translation of nested recursions. The separate theorem `PrintedHeight.height_agrees`
proves that this expansion equals the height used by the original proof.
Its compilation status must be read from the build receipt, not inferred from this text.


## initialHingeOrder

Source: `RequestProject\TypedTriangle\TowerThresholdInputs.lean:14`.

```lean
def initialHingeOrder (h : ℕ) : ℕ := 2*h-3
```

## compressionPowerMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:155`.

```lean
def compressionPowerMajorant (M : ℕ) : ℕ := 2^(M^2)
```

## hingeDensityMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:87`.

```lean
def hingeDensityMajorant (M : ℕ) : ℕ :=
  (M^3*M^(2*M+1))*((2048*M^2)*compressionPowerMajorant (2*M))
```

## normalizedDensityMajorant

Source: `RequestProject\TypedTriangle\TowerThresholdInputs.lean:18`.

```lean
def normalizedDensityMajorant (K : ℕ) : ℕ := max K (hingeDensityMajorant K)*8
```

## normalizedInputScale

Source: `RequestProject\TypedTriangle\TowerThresholdInputs.lean:19`.

```lean
def normalizedInputScale (K : ℕ) : ℕ := K+2*K+normalizedDensityMajorant K+1
```

## thresholdWorkingScale

Source: `RequestProject\TypedTriangle\TowerThresholdInputs.lean:20`.

```lean
def thresholdWorkingScale (K : ℕ) : ℕ := normalizedInputScale K*32
```

## deletionBudgetMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryBudgets.lean:13`.

```lean
def deletionBudgetMajorant (M : ℕ) : ℕ := max 2 (M*(4*compressionPowerMajorant (M+1)))
```

## nestedBudgetMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryBudgets.lean:14`.

```lean
def nestedBudgetMajorant (M : ℕ) : ℕ :=
  max (deletionBudgetMajorant M) (M*(128*compressionPowerMajorant (M+1)))
```

## coreToleranceMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryBudgets.lean:26`.

```lean
def coreToleranceMajorant (M : ℕ) : ℕ := max (max (deletionBudgetMajorant M) (nestedBudgetMajorant M)) 2
```

## preparationToleranceMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryBudgets.lean:27`.

```lean
def preparationToleranceMajorant (M : ℕ) : ℕ :=
  max (max (nestedBudgetMajorant M) (coreToleranceMajorant M)) (max 2 (M*(2*compressionPowerMajorant M)))
```

## hingeRatioMajorant

Source: `RequestProject\TypedTriangle\TowerGlobalScalars.lean:10`.

```lean
def hingeRatioMajorant (M k : ℕ) : ℕ := M*(k*compressionPowerMajorant M)
```

## rawToleranceMajorant

Source: `RequestProject\TypedTriangle\TowerThresholdInputs.lean:21`.

```lean
def rawToleranceMajorant (M : ℕ) : ℕ :=
  max (preparationToleranceMajorant (M*4)) (max (hingeRatioMajorant M 4) (8*max 1 (2*M)))
```

## sampleLcMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:14`.

```lean
def sampleLcMajorant (M : ℕ) : ℕ := 30*M+1
```

## sampleAMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:15`.

```lean
def sampleAMajorant (M : ℕ) : ℕ := 3*M*(27*M^3+1+M)+M
```

## sampleTMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:16`.

```lean
def sampleTMajorant (M : ℕ) : ℕ := 6*sampleAMajorant M*M+1
```

## sampleJMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:17`.

```lean
def sampleJMajorant (M : ℕ) : ℕ :=
  max (4*M) (max (12*(sampleLcMajorant M+1)*M)
    (6*(sampleLcMajorant M+1)*(sampleTMajorant M+1)*M))+1
```

## sampleEtaMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:20`.

```lean
def sampleEtaMajorant (M : ℕ) : ℕ := 2^sampleJMajorant M
```

## sampleLMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:21`.

```lean
def sampleLMajorant (M : ℕ) : ℕ := 2*M*sampleEtaMajorant M+1
```

## compressionClipMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:154`.

```lean
def compressionClipMajorant (M : ℕ) : ℕ := M+1
```

## compressionThetaMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:156`.

```lean
def compressionThetaMajorant (M : ℕ) : ℕ := compressionClipMajorant M*(64*compressionPowerMajorant M)
```

## compressionKappaMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:157`.

```lean
def compressionKappaMajorant (M : ℕ) : ℕ :=
  max ((compressionClipMajorant M*2)*4)
    (((compressionThetaMajorant M*4)*(compressionThetaMajorant M*2))*16)
```

## compressionPrecisionMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:160`.

```lean
def compressionPrecisionMajorant (M : ℕ) : ℕ :=
  (compressionClipMajorant M*compressionThetaMajorant M)*16
```

## compressionInitialMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:162`.

```lean
def compressionInitialMajorant (M : ℕ) : ℕ :=
  32*(compressionClipMajorant M*compressionThetaMajorant M^2)
```

## compressionInputMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:164`.

```lean
def compressionInputMajorant (M : ℕ) : ℕ :=
  2*compressionClipMajorant M+compressionKappaMajorant M+
    compressionPrecisionMajorant M+compressionInitialMajorant M+1
```

## sampleQMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:22`.

```lean
def sampleQMajorant (M : ℕ) : ℕ :=
  9*sampleLMajorant M*M*sampleEtaMajorant M*M+1+M
```

## sampleBMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:24`.

```lean
def sampleBMajorant (M : ℕ) : ℕ :=
  sampleLcMajorant M*(sampleJMajorant M+sampleTMajorant M)
```

## compressionSampleMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:168`.

```lean
def compressionSampleMajorant (M : ℕ) : ℕ :=
  sampleLMajorant (compressionInputMajorant M)*sampleQMajorant (compressionInputMajorant M)+
    sampleBMajorant (compressionInputMajorant M)
```

## physicalRankMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:19`.

```lean
def physicalRankMajorant (M : ℕ) : ℕ := (compressionSampleMajorant M+1)^2
```

## preparationRankMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:25`.

```lean
def preparationRankMajorant (M : ℕ) : ℕ := physicalRankMajorant (M*2)
```

## rawRankMajorant

Source: `RequestProject\TypedTriangle\TowerThresholdInputs.lean:23`.

```lean
def rawRankMajorant (M : ℕ) : ℕ := preparationRankMajorant (M*4)
```

## explicitTorsionRadius

Source: `RequestProject\TypedTriangle\QuotientBoxExplicitBound.lean:10`.

```lean
def explicitTorsionRadius (d R : ℕ) : ℕ := R * (2 * R + 1) ^ d
```

## explicitTorsionBound

Source: `RequestProject\TypedTriangle\QuotientBoxExplicitBound.lean:11`.

```lean
def explicitTorsionBound (d R : ℕ) : ℕ := (2 * explicitTorsionRadius d R + 1) ^ d
```

## compL2Majorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:15`.

```lean
def compL2Majorant (M : ℕ) : ℕ := 2*(3*(2*M))+1
```

## compNMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:16`.

```lean
def compNMajorant (M : ℕ) : ℕ := 4+24*compL2Majorant M
```

## compDMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:17`.

```lean
def compDMajorant (M s : ℕ) : ℕ := 16*compNMajorant M+96*(2*s+1)*compNMajorant M
```

## physicalColumnMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:20`.

```lean
def physicalColumnMajorant (M : ℕ) : ℕ :=
  3*compDMajorant (compressionClipMajorant M) (compressionSampleMajorant M)
```

## physicalTorsionMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:22`.

```lean
def physicalTorsionMajorant (M : ℕ) : ℕ :=
  max 1 (explicitTorsionBound (physicalRankMajorant M) (physicalColumnMajorant M))
```

## preparationTorsionMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:26`.

```lean
def preparationTorsionMajorant (M : ℕ) : ℕ := physicalTorsionMajorant (M*2)
```

## rawTorsionMajorant

Source: `RequestProject\TypedTriangle\TowerThresholdInputs.lean:24`.

```lean
def rawTorsionMajorant (M : ℕ) : ℕ := preparationTorsionMajorant (M*4)
```

## rawLengthMajorant

Source: `RequestProject\TypedTriangle\TowerThresholdInputs.lean:25`.

```lean
def rawLengthMajorant (M : ℕ) : ℕ := rawRankMajorant M+(rawRankMajorant M+1)*rawTorsionMajorant M
```

## oddPathMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPaths.lean:12`.

```lean
def oddPathMajorant (M : ℕ) : ℕ := 2*(4*((M+1)^2*(M+1)^5))+1
```

## nativeRhoMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPaths.lean:51`.

```lean
def nativeRhoMajorant (M : ℕ) : ℕ := max 1 (M*(8*compressionPowerMajorant M))
```

## nativeKappaMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPaths.lean:52`.

```lean
def nativeKappaMajorant (M : ℕ) : ℕ := nativeRhoMajorant M^2*2
```

## nativePathInputMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPaths.lean:53`.

```lean
def nativePathInputMajorant (M : ℕ) : ℕ := M+nativeKappaMajorant M+1
```

## nativeInteriorMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPaths.lean:54`.

```lean
def nativeInteriorMajorant (M : ℕ) : ℕ := oddPathMajorant (nativePathInputMajorant M)+1
```

## pathDensityMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPaths.lean:13`.

```lean
def pathDensityMajorant (M : ℕ) : ℕ := (M+1)^(oddPathMajorant M+3)*4
```

## nativeDensityMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPaths.lean:55`.

```lean
def nativeDensityMajorant (M : ℕ) : ℕ := pathDensityMajorant (nativePathInputMajorant M)
```

## nativeAvoidMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPaths.lean:56`.

```lean
def nativeAvoidMajorant (M : ℕ) : ℕ := nativeDensityMajorant M*(4*nativeInteriorMajorant M)
```

## nativeOuterAvoidMajorant

Source: `RequestProject\TypedTriangle\TowerThresholdInputs.lean:26`.

```lean
def nativeOuterAvoidMajorant (M : ℕ) : ℕ := max (nativeAvoidMajorant M) (max (M*2) 2)
```

## referenceProviderBound

Source: `RequestProject\TypedTriangle\TowerReferenceBudgets.lean:11`.

```lean
def referenceProviderBound (M : ℕ) : ℕ :=
  let Z := compressionPowerMajorant M * (M*2)
  let A := 1+3*(2*M)
  Z*(A+A^2)*(1+2*(1+3*(2*M)+3*Z))
```

## referenceSeedBudgetBound

Source: `RequestProject\TypedTriangle\TowerReferenceBudgets.lean:16`.

```lean
def referenceSeedBudgetBound (M : ℕ) : ℕ :=
  max (M*(10*compressionPowerMajorant M))
    (max (32*M) (M*(2*(16*M+4)*(referenceProviderBound (2*M)+1))))
```

## hingeBudgetMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryBudgets.lean:17`.

```lean
def hingeBudgetMajorant (M : ℕ) : ℕ := M*(64*compressionPowerMajorant M)
```

## geometryBudgetMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryBudgets.lean:18`.

```lean
def geometryBudgetMajorant (M : ℕ) : ℕ := max (M*4) (hingeBudgetMajorant M)
```

## latticeBudgetMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryBudgets.lean:16`.

```lean
def latticeBudgetMajorant (M : ℕ) : ℕ := M*(8*compressionPowerMajorant M)
```

## initialComplementMajorant

Source: `RequestProject\TypedTriangle\TowerThresholdInputs.lean:27`.

```lean
def initialComplementMajorant (M : ℕ) : ℕ :=
  max (referenceSeedBudgetBound M) (max (geometryBudgetMajorant M) (latticeBudgetMajorant M))
```

## referencePrecisionBound

Source: `RequestProject\TypedTriangle\TowerReferenceBudgets.lean:21`.

```lean
def referencePrecisionBound (M : ℕ) : ℕ := max (M*2) 2
```

## referenceToleranceBound

Source: `RequestProject\TypedTriangle\TowerReferenceBudgets.lean:22`.

```lean
def referenceToleranceBound (M : ℕ) : ℕ := referencePrecisionBound M*8
```

## referenceWeightBound

Source: `RequestProject\TypedTriangle\TowerReferenceBudgets.lean:24`.

```lean
def referenceWeightBound (M : ℕ) : ℕ := M+M*2
```

## referenceAvoidBound

Source: `RequestProject\TypedTriangle\TowerReferenceBudgets.lean:25`.

```lean
def referenceAvoidBound (M : ℕ) : ℕ := max (M*2) (referenceToleranceBound M*(8*referenceWeightBound M))
```

## resourceStockMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:195`.

```lean
def resourceStockMajorant (M : ℕ) : ℕ := referenceAvoidBound (8*M)
```

## supplyBudgetBound

Source: `RequestProject\TypedTriangle\TowerNatTerminal.lean:76`.

```lean
def supplyBudgetBound (M h : ℕ) : ℕ := max (max M 2) (M*(40*2^(h.choose 2)))
```

## cellDegreeBudgetBound

Source: `RequestProject\TypedTriangle\TowerBankBudgets.lean:13`.

```lean
def cellDegreeBudgetBound (M h : ℕ) : ℕ := max (M*8) (supplyBudgetBound (M*2) h*2)
```

## bankProtectionBound

Source: `RequestProject\TypedTriangle\TowerBankBudgets.lean:14`.

```lean
def bankProtectionBound (M h : ℕ) : ℕ := cellDegreeBudgetBound M h*2
```

## cleanHingeOrderMajorant

Source: `RequestProject\TypedTriangle\TowerThresholdInputs.lean:29`.

```lean
def cleanHingeOrderMajorant (M : ℕ) : ℕ := max (48*M) (8*(M+6)*compressionPowerMajorant M*M)
```

## thresholdInputMajorant

Source: `RequestProject\TypedTriangle\TowerThresholdInputs.lean:30`.

```lean
def thresholdInputMajorant (K hOriginal : ℕ) : ℕ :=
  let M := thresholdWorkingScale K
  M+rawToleranceMajorant M+rawRankMajorant M+rawTorsionMajorant M+rawLengthMajorant M+
    nativeInteriorMajorant M+nativeDensityMajorant M+nativeOuterAvoidMajorant M+
    initialComplementMajorant M+resourceStockMajorant M+
    bankProtectionBound M (initialHingeOrder hOriginal)+cleanHingeOrderMajorant K+1
```

## triangleThresholdInputBase

Source: `RequestProject\TypedTriangle\TowerTriangleThresholdAgenda.lean:26`.

```lean
def triangleThresholdInputBase (K h q : ℕ) : ℕ :=
  let M := thresholdInputMajorant K h
  M+32*M+4*K+q+1
```

## layerComplementBudgetMajorant

Source: `RequestProject\TypedTriangle\TowerBankLayerOrders.lean:19`.

```lean
def layerComplementBudgetMajorant (M : ℕ) : ℕ :=
  max (referenceSeedBudgetBound M) (max (geometryBudgetMajorant M) (latticeBudgetMajorant M))
```

## seedPointwisePlusTwoMajorant

Source: `RequestProject\TypedTriangle\TowerTrianglePacking.lean:22`.

```lean
def seedPointwisePlusTwoMajorant (M : ℕ) : ℕ :=
  (16*M+4)*referenceProviderBound (2*M)+2
```

## triangleComplementMajorant

Source: `RequestProject\TypedTriangle\TowerTrianglePacking.lean:24`.

```lean
def triangleComplementMajorant (M : ℕ) : ℕ :=
  max (layerComplementBudgetMajorant M) (max (referenceSeedBudgetBound M)
    (max M (M*seedPointwisePlusTwoMajorant M)))
```

## triangleThresholdInputMajorant

Source: `RequestProject\TypedTriangle\TowerTriangleThresholdAgenda.lean:30`.

```lean
def triangleThresholdInputMajorant (K h q : ℕ) : ℕ :=
  let U := triangleThresholdInputBase K h q
  U+triangleComplementMajorant U+1
```

## thresholdDensityScale

Source: `RequestProject\TypedTriangle\TowerThresholdAgenda.lean:19`.

```lean
def thresholdDensityScale (M : ℕ) : ℕ := M+8*M+1
```

## envelopeLoadBound

Source: `RequestProject\TypedTriangle\TowerReferenceBudgets.lean:26`.

```lean
def envelopeLoadBound (M : ℕ) : ℕ := 4*M+1
```

## envelopeBudgetBound

Source: `RequestProject\TypedTriangle\TowerReferenceBudgets.lean:28`.

```lean
def envelopeBudgetBound (M : ℕ) : ℕ := M*(64*(envelopeLoadBound M+4))
```

## referenceStockBudgetBound

Source: `RequestProject\TypedTriangle\TowerReferenceBudgets.lean:20`.

```lean
def referenceStockBudgetBound (M : ℕ) : ℕ := max (referenceSeedBudgetBound M) (8*M)
```

## envelopeDegreeBound

Source: `RequestProject\TypedTriangle\TowerReferenceBudgets.lean:27`.

```lean
def envelopeDegreeBound (M : ℕ) : ℕ := 2+2*envelopeLoadBound M
```

## prescribedBudgetBound

Source: `RequestProject\TypedTriangle\TowerReferenceBudgets.lean:30`.

```lean
def prescribedBudgetBound (M : ℕ) : ℕ :=
  max (envelopeBudgetBound M) (referenceStockBudgetBound M*(2*(envelopeDegreeBound M+1)))
```

## futureDensityMajorant

Source: `RequestProject\TypedTriangle\TowerReferenceAgenda.lean:14`.

```lean
def futureDensityMajorant (M : ℕ) : ℕ := prescribedBudgetBound (12*M)
```

## thresholdGlobalScale

Source: `RequestProject\TypedTriangle\TowerThresholdAgenda.lean:20`.

```lean
def thresholdGlobalScale (M : ℕ) : ℕ :=
  let U := thresholdDensityScale M
  U+futureDensityMajorant U+1
```

## pathRatioMajorant

Source: `RequestProject\TypedTriangle\TowerGlobalScalars.lean:9`.

```lean
def pathRatioMajorant (M k : ℕ) : ℕ := M*(k*M*2^M)
```

## uniformInnerRateMajorant

Source: `RequestProject\TypedTriangle\TowerGlobalScalars.lean:11`.

```lean
def uniformInnerRateMajorant (M : ℕ) : ℕ :=
  max 32 (max (M*4) (max (M*2) (max (M*16) (max (M*8)
    (max (hingeRatioMajorant M 64) (pathRatioMajorant M 64))))))
```

## adjustedBankWindowMajorant

Source: `RequestProject\TypedTriangle\TowerGlobalScalars.lean:14`.

```lean
def adjustedBankWindowMajorant (M : ℕ) : ℕ := max M (pathRatioMajorant M 32)
```

## globalInnerInputMajorant

Source: `RequestProject\TypedTriangle\TowerGlobalScalars.lean:15`.

```lean
def globalInnerInputMajorant (M : ℕ) : ℕ := max M (adjustedBankWindowMajorant M)
```

## globalInnerRateMajorant

Source: `RequestProject\TypedTriangle\TowerGlobalScalars.lean:16`.

```lean
def globalInnerRateMajorant (M : ℕ) : ℕ := uniformInnerRateMajorant (globalInnerInputMajorant M)
```

## windowRouteRateMajorant

Source: `RequestProject\TypedTriangle\TowerGlobalScalars.lean:17`.

```lean
def windowRouteRateMajorant (M : ℕ) : ℕ := M*M*(32*(M+1)*4^M)
```

## stateHoleCapMajorant

Source: `RequestProject\TypedTriangle\TowerGlobalScalars.lean:18`.

```lean
def stateHoleCapMajorant (M : ℕ) : ℕ := max (windowRouteRateMajorant M*4) (M*M*128)
```

## assemblyStateInputMajorant

Source: `RequestProject\TypedTriangle\TowerGlobalScalars.lean:24`.

```lean
def assemblyStateInputMajorant (M : ℕ) : ℕ := max M (globalInnerRateMajorant M)
```

## assemblyStateMajorant

Source: `RequestProject\TypedTriangle\TowerGlobalScalars.lean:25`.

```lean
def assemblyStateMajorant (M : ℕ) : ℕ := stateHoleCapMajorant (assemblyStateInputMajorant M)
```

## preparationDebtMajorant

Source: `RequestProject\TypedTriangle\TowerGlobalScalars.lean:19`.

```lean
def preparationDebtMajorant (M : ℕ) : ℕ :=
  max M (max M (max (hingeRatioMajorant M 4) (8*max 1 (2*M))))
```

## globalDebtMajorant

Source: `RequestProject\TypedTriangle\TowerGlobalScalars.lean:21`.

```lean
def globalDebtMajorant (M : ℕ) : ℕ :=
  max 8 (max (M*128) (max (pathRatioMajorant M 64)
    (max (pathRatioMajorant M 128) (preparationDebtMajorant M))))
```

## thresholdRadiusScale

Source: `RequestProject\TypedTriangle\TowerThresholdAgenda.lean:23`.

```lean
def thresholdRadiusScale (M : ℕ) : ℕ :=
  let V := thresholdGlobalScale M
  V+globalInnerRateMajorant V+assemblyStateMajorant V+2*globalDebtMajorant V+1
```

## radiusNextCap

Source: `RequestProject\TypedTriangle\TowerRadiusBounds.lean:10`.

```lean
def radiusNextCap (K : ℕ) : ℕ := max (K*2) (K*(16*K*(K+1)))*2
```

## radiusInputCap

Source: `RequestProject\TypedTriangle\TowerRadiusBounds.lean:11`.

```lean
def radiusInputCap (K : ℕ) : ℕ := K+radiusNextCap K+1
```

## radiusMajorant

Source: `RequestProject\TypedTriangle\TowerRadiusBounds.lean:12`.

```lean
def radiusMajorant (F : ℕ → ℕ) (M : ℕ) : ℕ → ℕ
  | 0 => M+F M
  | r+1 => let U := radiusInputCap (radiusMajorant F M r); U+F U
```

## kernelCapMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:124`.

```lean
def kernelCapMajorant (M : ℕ) : ℕ := max 1 ((compressionPowerMajorant M*2)*M)
```

## smoothCoefficientMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:126`.

```lean
def smoothCoefficientMajorant (M : ℕ) : ℕ :=
  let D := 12*kernelCapMajorant M
  6*M+((3*M)*2)*(14*(3*D^2+D^3*3)+36*M^2)
```

## natKernel

Source: `RequestProject\TypedTriangle\TowerNatAlgebra.lean:10`.

```lean
def natKernel : ℕ → ℕ → ℕ
  | 0, _ => 1
  | d+1, R => (2*R+1)*natKernel d (R*(2*R+1))
```

## natSolver

Source: `RequestProject\TypedTriangle\TowerNatAlgebra.lean:14`.

```lean
def natSolver : ℕ → ℕ → ℕ
  | 0, _ => 0
  | d+1, K => (1+2*(d+1)*(max 1 K)^2)*(natSolver d (2*(max 1 K)^2)+1)
```

## natStep

Source: `RequestProject\TypedTriangle\TowerNatAlgebra.lean:92`.

```lean
def natStep (M : ℕ) : ℕ :=
  (M+1)+(M+1)^2+(M+1)^(M+1)+(M+1).factorial+natKernel M M+natSolver M M
```

## natEnvelope

Source: `RequestProject\TypedTriangle\TowerNatAlgebra.lean:143`.

```lean
def natEnvelope : ℕ → ℕ → ℕ
  | 0, M => M+2
  | k+1, M => natStep (natEnvelope k M)
```

## compHMajorant

Source: `RequestProject\TypedTriangle\TowerUniformCertificate.lean:12`.

```lean
def compHMajorant (M S : ℕ) : ℕ :=
  1+8*compL2Majorant M+5*compNMajorant M+32*(2*S+1)*compNMajorant M
```

## uniformCertMajorant

Source: `RequestProject\TypedTriangle\TowerUniformCertificate.lean:15`.

```lean
def uniformCertMajorant (M : ℕ) : ℕ :=
  let S := compressionSampleMajorant M
  natEnvelope 6 (S+compHMajorant M S+compDMajorant M S)
```

## smoothSampleMajorant

Source: `RequestProject\TypedTriangle\TowerSmoothBounds.lean:12`.

```lean
def smoothSampleMajorant (M : ℕ) : ℕ := compressionSampleMajorant (2*M)
```

## smoothDMajorant

Source: `RequestProject\TypedTriangle\TowerSmoothBounds.lean:13`.

```lean
def smoothDMajorant (M : ℕ) : ℕ := compDMajorant (2*M) (smoothSampleMajorant M)
```

## routingCompMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:120`.

```lean
def routingCompMajorant (M : ℕ) : ℕ := M+1
```

## routeDMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:121`.

```lean
def routeDMajorant (M : ℕ) : ℕ := 12*routingCompMajorant M^2
```

## smoothDemandMajorant

Source: `RequestProject\TypedTriangle\TowerSmoothBounds.lean:14`.

```lean
def smoothDemandMajorant (M : ℕ) : ℕ :=
  let S := smoothSampleMajorant M
  let D := smoothDMajorant M
  let R := routeDMajorant (2*M)
  3*R*natKernel ((S+1)^2) (max (D*(3*R)) (3*D))
```

## smoothCertMajorant

Source: `RequestProject\TypedTriangle\TowerSmoothBounds.lean:19`.

```lean
def smoothCertMajorant (M : ℕ) : ℕ := uniformCertMajorant (4*M)*smoothDemandMajorant M
```

## routeBudgetMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:122`.

```lean
def routeBudgetMajorant (M : ℕ) : ℕ := max (M*(8*compressionPowerMajorant M)) (routingCompMajorant M)
```

## congestionMajorant

Source: `RequestProject\TypedTriangle\TowerSmoothBounds.lean:21`.

```lean
def congestionMajorant (M : ℕ) : ℕ :=
  let K := smoothCertMajorant M
  let D := routeDMajorant (2*M)
  let δ := routeBudgetMajorant (2*M)
  K*(4*D+3+32*D*δ+12*K*M+2*D+2)+1
```

## inverseCostMajorant

Source: `RequestProject\TypedTriangle\TowerSmoothBounds.lean:27`.

```lean
def inverseCostMajorant (M : ℕ) : ℕ := smoothCoefficientMajorant (M+congestionMajorant M)
```

## paidDensityMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:89`.

```lean
def paidDensityMajorant (M : ℕ) : ℕ := max (M*2) (hingeDensityMajorant M)
```

## paidSmoothInputMajorant

Source: `RequestProject\TypedTriangle\TowerSmoothBounds.lean:31`.

```lean
def paidSmoothInputMajorant (M : ℕ) : ℕ :=
  M+paidDensityMajorant M+max M 2+2*M+1
```

## paidBudgetMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryBudgets.lean:19`.

```lean
def paidBudgetMajorant (M : ℕ) : ℕ := max (geometryBudgetMajorant M*2) (latticeBudgetMajorant M*2)
```

## paidCostMajorant

Source: `RequestProject\TypedTriangle\TowerSmoothBounds.lean:33`.

```lean
def paidCostMajorant (M : ℕ) : ℕ :=
  max (inverseCostMajorant (paidSmoothInputMajorant M)) (paidBudgetMajorant M)
```

## referenceLoadBound

Source: `RequestProject\TypedTriangle\TowerReferenceBudgets.lean:23`.

```lean
def referenceLoadBound (M : ℕ) : ℕ := max (referenceToleranceBound M*4) 4
```

## prescribedLoadBound

Source: `RequestProject\TypedTriangle\TowerReferenceBudgets.lean:32`.

```lean
def prescribedLoadBound (M : ℕ) : ℕ := max (referenceLoadBound M) 2
```

## referencePrecisionMajorant

Source: `RequestProject\TypedTriangle\TowerReferenceAgenda.lean:15`.

```lean
def referencePrecisionMajorant (M : ℕ) : ℕ :=
  max M (max (M*(10*compressionPowerMajorant M))
    (max (paidBudgetMajorant M*4) (512*M*M*paidCostMajorant M)))
```

## referenceLoadMajorant

Source: `RequestProject\TypedTriangle\TowerReferenceAgenda.lean:19`.

```lean
def referenceLoadMajorant (M : ℕ) : ℕ := prescribedLoadBound (referencePrecisionMajorant M)
```

## profileToleranceMajorant

Source: `RequestProject\TypedTriangle\TowerReferenceAgenda.lean:22`.

```lean
def profileToleranceMajorant (M : ℕ) : ℕ :=
  max (2*M*paidCostMajorant M) (referenceLoadMajorant M)
```

## innerRadiusInput

Source: `RequestProject\TypedTriangle\TowerReferenceAgenda.lean:24`.

```lean
def innerRadiusInput (M : ℕ) : ℕ := M+2*M+max M (M*(2*(M+1)))+1
```

## innerRadiusMajorant

Source: `RequestProject\TypedTriangle\TowerReferenceAgenda.lean:25`.

```lean
def innerRadiusMajorant (M : ℕ) : ℕ :=
  radiusMajorant profileToleranceMajorant (innerRadiusInput M) M
```

## geometryOrderMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryBudgets.lean:21`.

```lean
def geometryOrderMajorant (M : ℕ) : ℕ := 128*(M+2)*compressionPowerMajorant M*M+1
```

## latticeOrderMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryBudgets.lean:22`.

```lean
def latticeOrderMajorant (M : ℕ) : ℕ := 4*M+1
```

## paidOrderMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryBudgets.lean:23`.

```lean
def paidOrderMajorant (M : ℕ) : ℕ := max (geometryOrderMajorant M) (latticeOrderMajorant M)
```

## compressionOrderMajorant

Source: `RequestProject\TypedTriangle\TowerGeometrySample.lean:172`.

```lean
def compressionOrderMajorant (M : ℕ) : ℕ :=
  4*compressionClipMajorant M+4*M*compressionPowerMajorant M*compressionClipMajorant M+1
```

## paidPreparedInputMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:90`.

```lean
def paidPreparedInputMajorant (M : ℕ) : ℕ := paidDensityMajorant M*4+2*M+1
```

## paidPreparedOrderMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:91`.

```lean
def paidPreparedOrderMajorant (M : ℕ) : ℕ := compressionOrderMajorant (paidPreparedInputMajorant M)
```

## routeOrderMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:123`.

```lean
def routeOrderMajorant (M : ℕ) : ℕ := (8+4*M*compressionPowerMajorant M)*M+1
```

## nZeroMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:125`.

```lean
def nZeroMajorant (M : ℕ) : ℕ := 2*(12*M+3)*compressionPowerMajorant M*M
```

## inverseOrderMajorant

Source: `RequestProject\TypedTriangle\TowerSmoothBounds.lean:28`.

```lean
def inverseOrderMajorant (M : ℕ) : ℕ :=
  max (max (compressionOrderMajorant (4*M))
    (max (compressionOrderMajorant (2*M)) (routeOrderMajorant (2*M)))) (nZeroMajorant M)
```

## paidInverseOrderMajorant

Source: `RequestProject\TypedTriangle\TowerSmoothBounds.lean:35`.

```lean
def paidInverseOrderMajorant (M : ℕ) : ℕ := inverseOrderMajorant (paidSmoothInputMajorant M)
```

## envelopeOrderBound

Source: `RequestProject\TypedTriangle\TowerReferenceBudgets.lean:29`.

```lean
def envelopeOrderBound (M : ℕ) : ℕ := 32*envelopeLoadBound M*M+1
```

## analyticCutBound

Source: `RequestProject\TypedTriangle\TowerAnalyticCuts.lean:14`.

```lean
def analyticCutBound (M : ℕ) : ℕ := (2 * M * M) ^ (2 * M)
```

## nibbleThreeBound

Source: `RequestProject\TypedTriangle\TowerAnalyticPacking.lean:13`.

```lean
def nibbleThreeBound : ℕ := analyticCutBound 1000000
```

## egjFourInputBound

Source: `RequestProject\TypedTriangle\TowerAnalyticClone.lean:52`.

```lean
def egjFourInputBound : ℕ := 30000000 + 2 * nibbleThreeBound
```

## egjFourBound

Source: `RequestProject\TypedTriangle\TowerAnalyticClone.lean:53`.

```lean
def egjFourBound : ℕ := analyticCutBound egjFourInputBound
```

## cloneInputBound

Source: `RequestProject\TypedTriangle\TowerAnalyticClone.lean:96`.

```lean
def cloneInputBound (M : ℕ) : ℕ :=
  max 5120000 (max egjFourBound (4*M*M+2))
```

## cloneBound

Source: `RequestProject\TypedTriangle\TowerAnalyticClone.lean:99`.

```lean
def cloneBound (M : ℕ) : ℕ := analyticCutBound (cloneInputBound M)
```

## approxPackingBound

Source: `RequestProject\TypedTriangle\TowerAnalyticClone.lean:163`.

```lean
def approxPackingBound (M : ℕ) : ℕ := cloneBound (16*M)
```

## referenceOrderInput

Source: `RequestProject\TypedTriangle\TowerReferenceOrders.lean:11`.

```lean
def referenceOrderInput (M : ℕ) : ℕ := 1+referenceWeightBound M+referencePrecisionBound M
```

## referenceOrderBound

Source: `RequestProject\TypedTriangle\TowerReferenceOrders.lean:12`.

```lean
def referenceOrderBound (M : ℕ) : ℕ :=
  max (max (16*M+1) (approxPackingBound (referenceOrderInput M))) 1
```

## prescribedOrderBound

Source: `RequestProject\TypedTriangle\TowerReferenceOrders.lean:14`.

```lean
def prescribedOrderBound (M : ℕ) : ℕ :=
  max (envelopeOrderBound M) (max (referenceOrderBound M)
    (2*envelopeDegreeBound M*referenceStockBudgetBound M))
```

## referenceAgendaInput

Source: `RequestProject\TypedTriangle\TowerReferenceAgenda.lean:18`.

```lean
def referenceAgendaInput (M : ℕ) : ℕ := 12*M+referencePrecisionMajorant M
```

## referenceThresholdMajorant

Source: `RequestProject\TypedTriangle\TowerReferenceAgenda.lean:21`.

```lean
def referenceThresholdMajorant (M : ℕ) : ℕ := prescribedOrderBound (referenceAgendaInput M)
```

## innerNodeOrderMajorant

Source: `RequestProject\TypedTriangle\TowerReferenceAgenda.lean:27`.

```lean
def innerNodeOrderMajorant (M : ℕ) : ℕ :=
  max (max (max (paidOrderMajorant M) (paidPreparedOrderMajorant M))
    (paidInverseOrderMajorant M)) (referenceThresholdMajorant M)
```

## innerScheduleMajorant

Source: `RequestProject\TypedTriangle\TowerReferenceAgenda.lean:30`.

```lean
def innerScheduleMajorant (M : ℕ) : ℕ :=
  max (paidOrderMajorant M) (innerNodeOrderMajorant (M+innerRadiusMajorant M))
```

## thresholdProfileScale

Source: `RequestProject\TypedTriangle\TowerThresholdAgenda.lean:26`.

```lean
def thresholdProfileScale (M : ℕ) : ℕ :=
  let W := thresholdRadiusScale M
  W+innerRadiusMajorant W+innerScheduleMajorant W+1
```

## prescribedAvoidBound

Source: `RequestProject\TypedTriangle\TowerReferenceBudgets.lean:33`.

```lean
def prescribedAvoidBound (M : ℕ) : ℕ := max (referenceAvoidBound M) (envelopeBudgetBound M)
```

## referenceAvoidMajorant

Source: `RequestProject\TypedTriangle\TowerReferenceAgenda.lean:20`.

```lean
def referenceAvoidMajorant (M : ℕ) : ℕ := prescribedAvoidBound (referenceAgendaInput M)
```

## thresholdAgendaMajorant

Source: `RequestProject\TypedTriangle\TowerThresholdAgenda.lean:29`.

```lean
def thresholdAgendaMajorant (M : ℕ) : ℕ :=
  let P := thresholdProfileScale M
  P+paidCostMajorant P+referenceLoadMajorant P+referenceAvoidMajorant P+
    referenceThresholdMajorant P+paidInverseOrderMajorant P+paidOrderMajorant P+1
```

## catalogDimensionMajorant

Source: `RequestProject\TypedTriangle\TowerBankCatalog.lean:9`.

```lean
def catalogDimensionMajorant (M : ℕ) : ℕ := (compressionSampleMajorant M+1)^2
```

## catalogCoefficientMajorant

Source: `RequestProject\TypedTriangle\TowerBankCatalog.lean:10`.

```lean
def catalogCoefficientMajorant (M : ℕ) : ℕ :=
  compDMajorant (compressionClipMajorant M) (compressionSampleMajorant M)
```

## catalogColumnMajorant

Source: `RequestProject\TypedTriangle\TowerBankCatalog.lean:12`.

```lean
def catalogColumnMajorant (M : ℕ) : ℕ := 3*catalogCoefficientMajorant M
```

## atomRadiusMajorant

Source: `RequestProject\TypedTriangle\TowerBankCatalog.lean:13`.

```lean
def atomRadiusMajorant (M : ℕ) : ℕ := 3*routeDMajorant (M*2)
```

## bankCatalogInputMajorant

Source: `RequestProject\TypedTriangle\TowerBankCatalog.lean:14`.

```lean
def bankCatalogInputMajorant (M : ℕ) : ℕ :=
  atomRadiusMajorant M+catalogDimensionMajorant M+catalogCoefficientMajorant M+
    catalogColumnMajorant M+catalogDimensionMajorant (M*2)+
    catalogCoefficientMajorant (M*2)+catalogColumnMajorant (M*2)
```

## bankRadiusMajorant

Source: `RequestProject\TypedTriangle\TowerBankCatalog.lean:18`.

```lean
def bankRadiusMajorant (M : ℕ) : ℕ := natEnvelope 5 (bankCatalogInputMajorant M)
```

## bankCatalogSizeMajorant

Source: `RequestProject\TypedTriangle\TowerBankCatalog.lean:19`.

```lean
def bankCatalogSizeMajorant (M : ℕ) : ℕ := natEnvelope 8 (bankCatalogInputMajorant M)
```

## supplySizeBound

Source: `RequestProject\TypedTriangle\TowerNatTerminal.lean:104`.

```lean
def supplySizeBound (K h k : ℕ) : ℕ := K*k*(4*(2*h-2).choose 2+6)
```

## boundedPieceSizeMajorant

Source: `RequestProject\TypedTriangle\TowerBankCells.lean:11`.

```lean
def boundedPieceSizeMajorant (M h k : ℕ) : ℕ := supplySizeBound (uniformCertMajorant M) h k
```

## bankRerouteMajorant

Source: `RequestProject\TypedTriangle\TowerBankCatalog.lean:20`.

```lean
def bankRerouteMajorant (M : ℕ) : ℕ := natEnvelope 9 (bankCatalogInputMajorant M)
```

## bankCellSizeMajorant

Source: `RequestProject\TypedTriangle\TowerBankCells.lean:14`.

```lean
def bankCellSizeMajorant (M h : ℕ) : ℕ :=
  boundedPieceSizeMajorant (M*2) h (4*bankRerouteMajorant M)+4*bankRerouteMajorant M
```

## coreDeltaBound

Source: `RequestProject\TypedTriangle\TowerBankBudgets.lean:16`.

```lean
def coreDeltaBound (M h : ℕ) : ℕ := max 2 (M*(2*2^(h.choose 2)))
```

## nativeDeleteMajorant

Source: `RequestProject\TypedTriangle\TowerBankLayerOrders.lean:90`.

```lean
def nativeDeleteMajorant (M : ℕ) : ℕ := nativeRhoMajorant M*4
```

## bankToleranceBound

Source: `RequestProject\TypedTriangle\TowerBankBudgets.lean:15`.

```lean
def bankToleranceBound (M h : ℕ) : ℕ := max (bankProtectionBound M h) M
```

## quadraticRateMajorant

Source: `RequestProject\TypedTriangle\TowerBankCells.lean:20`.

```lean
def quadraticRateMajorant (M E B : ℕ) : ℕ := M*M*(32*(E*B+1))
```

## geometricDeletionBound

Source: `RequestProject\TypedTriangle\TowerBankBudgets.lean:17`.

```lean
def geometricDeletionBound (M h : ℕ) : ℕ := max 2 (M*(4*2^((h+1).choose 2)))
```

## cellDeletionBound

Source: `RequestProject\TypedTriangle\TowerBankBudgets.lean:18`.

```lean
def cellDeletionBound (M h : ℕ) : ℕ := max (geometricDeletionBound M h) (coreDeltaBound M h)
```

## bankDeletionBound

Source: `RequestProject\TypedTriangle\TowerBankBudgets.lean:19`.

```lean
def bankDeletionBound (M h : ℕ) : ℕ :=
  max (geometricDeletionBound M h) (max (max (cellDeletionBound M h) (coreDeltaBound M h)) M)
```

## bankCopiesMajorant

Source: `RequestProject\TypedTriangle\TowerBankCells.lean:18`.

```lean
def bankCopiesMajorant (M P : ℕ) : ℕ := 2*bankCatalogSizeMajorant M*P
```

## nativeBankRateMajorant

Source: `RequestProject\TypedTriangle\TowerBankCells.lean:22`.

```lean
def nativeBankRateMajorant (M h P : ℕ) : ℕ :=
  quadraticRateMajorant (max (bankToleranceBound M h) (bankDeletionBound M h))
    (bankCellSizeMajorant M h) (bankCopiesMajorant M P)
```

## preparedBankInputMajorant

Source: `RequestProject\TypedTriangle\TowerBankCells.lean:30`.

```lean
def preparedBankInputMajorant (M h : ℕ) : ℕ := max M (coreDeltaBound M h)
```

## preparedBankRateMajorant

Source: `RequestProject\TypedTriangle\TowerBankCells.lean:31`.

```lean
def preparedBankRateMajorant (M h P : ℕ) : ℕ := nativeBankRateMajorant (preparedBankInputMajorant M h) h P
```

## natExtensionCost

Source: `RequestProject\TypedTriangle\TowerNatMonitors.lean:191`.

```lean
def natExtensionCost (d D E R : ℕ) : ℕ := d*natSolver d (D*R+E)*R*D
```

## deletedExtensionMajorant

Source: `RequestProject\TypedTriangle\TowerBankWeights.lean:14`.

```lean
def deletedExtensionMajorant (M : ℕ) : ℕ :=
  let D := compDMajorant (M+1) (compressionSampleMajorant M)
  natExtensionCost (physicalRankMajorant M) D (3*D) (3*routeDMajorant M)
```

## physicalGlueMajorant

Source: `RequestProject\TypedTriangle\TowerBankWeights.lean:17`.

```lean
def physicalGlueMajorant (M : ℕ) : ℕ := deletedExtensionMajorant M+1
```

## physicalWeightMajorant

Source: `RequestProject\TypedTriangle\TowerBankWeights.lean:20`.

```lean
def physicalWeightMajorant (M : ℕ) : ℕ :=
  max ((1+4*(6*M^2+1))*physicalGlueMajorant M*(M*(M*M))) (M*(M*M))+1
```

## bankGammaBound

Source: `RequestProject\TypedTriangle\TowerBankBudgets.lean:9`.

```lean
def bankGammaBound (M : ℕ) : ℕ := M*M*8
```

## bankEtaBound

Source: `RequestProject\TypedTriangle\TowerBankBudgets.lean:10`.

```lean
def bankEtaBound (M B : ℕ) : ℕ := max (M*(M^2)*8) (bankGammaBound M*(B+1))
```

## monitorCapBound

Source: `RequestProject\TypedTriangle\TowerBankBudgets.lean:11`.

```lean
def monitorCapBound (M K : ℕ) : ℕ := (M*(K+1))*(2+15*M)
```

## forkEpsilonMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:138`.

```lean
def forkEpsilonMajorant (M : ℕ) : ℕ := M^2*(1024*(M+1))
```

## withdrawalKappaMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:140`.

```lean
def withdrawalKappaMajorant (M : ℕ) : ℕ := M*M*2
```

## selectorEpsilonMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:72`.

```lean
def selectorEpsilonMajorant (M B : ℕ) : ℕ := (M+1)^2*(10000*B)
```

## selectorAMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:71`.

```lean
def selectorAMajorant (M : ℕ) : ℕ := 200*M+8
```

## paymentGammaMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:15`.

```lean
def paymentGammaMajorant (M : ℕ) : ℕ := max (M*M*32) (M*8)
```

## paymentTMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:16`.

```lean
def paymentTMajorant (M : ℕ) : ℕ := M+61*M+61
```

## paymentCostMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:17`.

```lean
def paymentCostMajorant (M : ℕ) : ℕ := 2*(paymentGammaMajorant M+8)*paymentTMajorant M+4
```

## paymentInputMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:18`.

```lean
def paymentInputMajorant (M : ℕ) : ℕ :=
  max (M*M*(8*paymentCostMajorant M)) (M*(12*paymentTMajorant M))
```

## selectorQMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:73`.

```lean
def selectorQMajorant (M B : ℕ) : ℕ := 4*B*(M+1)+2
```

## selectorScale

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:74`.

```lean
def selectorScale (M : ℕ) : ℕ :=
  M+M*M*2+M*2+selectorAMajorant M+selectorQMajorant M (selectorAMajorant M)+1
```

## selectorInputMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:78`.

```lean
def selectorInputMajorant (M : ℕ) : ℕ :=
  max (selectorEpsilonMajorant M (selectorAMajorant M)) (paymentInputMajorant (selectorScale M))
```

## forkQMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:139`.

```lean
def forkQMajorant (M : ℕ) : ℕ := 128*M+1
```

## withdrawalKMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:141`.

```lean
def withdrawalKMajorant (M : ℕ) : ℕ := forkQMajorant (withdrawalKappaMajorant M)+6
```

## paymentForbiddenMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:14`.

```lean
def paymentForbiddenMajorant (M : ℕ) : ℕ := M*M*16
```

## selectorStockMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:76`.

```lean
def selectorStockMajorant (M : ℕ) : ℕ :=
  max (selectorEpsilonMajorant M (selectorAMajorant M)) (paymentForbiddenMajorant (selectorScale M))
```

## withdrawalInputMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:144`.

```lean
def withdrawalInputMajorant (M : ℕ) : ℕ :=
  max (forkEpsilonMajorant (withdrawalKappaMajorant M))
    (max (max (selectorInputMajorant (2*M)) (M*2)*(4*withdrawalKMajorant M))
      (selectorStockMajorant M*(8*withdrawalKMajorant M)))
```

## resourceOutputMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:199`.

```lean
def resourceOutputMajorant (M : ℕ) : ℕ := max (M*M*16) M
```

## resourceInputScale

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:200`.

```lean
def resourceInputScale (M : ℕ) : ℕ := M+resourceOutputMajorant M+1
```

## resourceInputMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:201`.

```lean
def resourceInputMajorant (M : ℕ) : ℕ :=
  max (withdrawalInputMajorant (resourceInputScale M)*4) (max (resourceOutputMajorant M) M)
```

## resourceCompletionMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:203`.

```lean
def resourceCompletionMajorant (M : ℕ) : ℕ :=
  M*2*(max (resourceInputMajorant M*12) 2)^2*2
```

## samplingPrecisionMajorant

Source: `RequestProject\TypedTriangle\TowerBankResourceOrders.lean:14`.

```lean
def samplingPrecisionMajorant (M : ℕ) : ℕ := max (M^2*4) (M*M^4*128)
```

## basalSamplingMajorant

Source: `RequestProject\TypedTriangle\TowerBankResourceOrders.lean:15`.

```lean
def basalSamplingMajorant (M : ℕ) : ℕ := 96*samplingPrecisionMajorant M^4+1
```

## stockRateMajorant

Source: `RequestProject\TypedTriangle\TowerBankResourceOrders.lean:16`.

```lean
def stockRateMajorant (M : ℕ) : ℕ := max (M*12) 2
```

## rawStockSamplingScale

Source: `RequestProject\TypedTriangle\TowerBankResourceOrders.lean:17`.

```lean
def rawStockSamplingScale (M : ℕ) : ℕ := M+stockRateMajorant M+M*2+1
```

## rawStockOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankResourceOrders.lean:18`.

```lean
def rawStockOrderMajorant (M : ℕ) : ℕ :=
  max (referenceOrderBound (8*M)) (basalSamplingMajorant (rawStockSamplingScale M))
```

## resourceStockOrderScale

Source: `RequestProject\TypedTriangle\TowerBankResourceOrders.lean:20`.

```lean
def resourceStockOrderScale (M : ℕ) : ℕ := M+resourceInputMajorant M+1
```

## paymentOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:20`.

```lean
def paymentOrderMajorant (M : ℕ) : ℕ := max (max (paymentInputMajorant M) (paymentGammaMajorant M)) 1
```

## selectorOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:80`.

```lean
def selectorOrderMajorant (M : ℕ) : ℕ :=
  max (paymentOrderMajorant (selectorScale M)) (200*(M+1))
```

## withdrawalOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:148`.

```lean
def withdrawalOrderMajorant (M : ℕ) : ℕ :=
  max (max (selectorOrderMajorant (2*M)) (32*withdrawalKappaMajorant M)) (withdrawalInputMajorant M)
```

## resourceOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankResourceOrders.lean:21`.

```lean
def resourceOrderMajorant (M : ℕ) : ℕ :=
  max (rawStockOrderMajorant (resourceStockOrderScale M))
    (max (withdrawalOrderMajorant (resourceInputScale M))
      (4*withdrawalInputMajorant (resourceInputScale M)))
```

## stockBankResourceScale

Source: `RequestProject\TypedTriangle\TowerBankLayerOrders.lean:26`.

```lean
def stockBankResourceScale (M h : ℕ) : ℕ := M+bankProtectionBound M h*2+1
```

## catalogCompressionOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankCatalog.lean:21`.

```lean
def catalogCompressionOrderMajorant (M : ℕ) : ℕ :=
  max (compressionOrderMajorant M) (2*compressionOrderMajorant (M*2))
```

## deletionNumerator

Source: `RequestProject\TypedTriangle\TowerNatTerminal.lean:77`.

```lean
def deletionNumerator (U h : ℕ) : ℕ := 8*((U+3)+(U+1+h)*2^(h.choose 2))
```

## deletionOrderBound

Source: `RequestProject\TypedTriangle\TowerNatTerminal.lean:78`.

```lean
def deletionOrderBound (M U h N : ℕ) : ℕ := deletionNumerator U h*M+1+2*N
```

## supplySupportBound

Source: `RequestProject\TypedTriangle\TowerNatTerminal.lean:105`.

```lean
def supplySupportBound (K h k : ℕ) : ℕ :=
  2*k+3*(K*k)+K*k*(2*h-2)+3*(K*k)*(2*h-3)
```

## supplyOrderBound

Source: `RequestProject\TypedTriangle\TowerNatTerminal.lean:107`.

```lean
def supplyOrderBound (M K h k : ℕ) : ℕ := deletionOrderBound M (supplySupportBound K h k) h 0
```

## boundedPieceOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankCells.lean:12`.

```lean
def boundedPieceOrderMajorant (M h k : ℕ) : ℕ :=
  max (compressionOrderMajorant M) (supplyOrderBound M (uniformCertMajorant M) h k)
```

## bankCellOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankCells.lean:16`.

```lean
def bankCellOrderMajorant (M h : ℕ) : ℕ :=
  2*boundedPieceOrderMajorant (M*2) h (4*bankRerouteMajorant M)+40*bankRerouteMajorant M*M+1
```

## atomCoreOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankCells.lean:19`.

```lean
def atomCoreOrderMajorant (M : ℕ) : ℕ := 2*(routeOrderMajorant (M*2)+(3*(M*2)+1))
```

## quadraticOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankCells.lean:21`.

```lean
def quadraticOrderMajorant (M E B : ℕ) : ℕ := max 1 (max (4*M) (max (2*M) (2*(B*E)*M)))
```

## nativeBankOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankCells.lean:25`.

```lean
def nativeBankOrderMajorant (M h P : ℕ) : ℕ :=
  max (catalogCompressionOrderMajorant M) (max (bankCellOrderMajorant M h)
    (max (atomCoreOrderMajorant M)
      (quadraticOrderMajorant (max (bankToleranceBound M h) (bankDeletionBound M h))
        (bankCellSizeMajorant M h) (bankCopiesMajorant M P))))
```

## preparedBankOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankCells.lean:32`.

```lean
def preparedBankOrderMajorant (M h P : ℕ) : ℕ :=
  max (nativeBankOrderMajorant (preparedBankInputMajorant M h) h P)
    (atomCoreOrderMajorant (preparedBankInputMajorant M h))
```

## stockBankOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankLayerOrders.lean:27`.

```lean
def stockBankOrderMajorant (M h : ℕ) : ℕ :=
  max (resourceOrderMajorant (stockBankResourceScale M h)) (2*preparedBankOrderMajorant M h M*M)
```

## layerComplementOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankLayerOrders.lean:21`.

```lean
def layerComplementOrderMajorant (M : ℕ) : ℕ :=
  max (16*M+1) (max (geometryOrderMajorant M) (latticeOrderMajorant M))
```

## monitoredPackingOrderBound

Source: `RequestProject\TypedTriangle\TowerPackingOrders.lean:10`.

```lean
def monitoredPackingOrderBound (M : ℕ) : ℕ := max 2 (cloneBound (3*M+2))
```

## packingSignedScale

Source: `RequestProject\TypedTriangle\TowerPackingOrders.lean:11`.

```lean
def packingSignedScale (M : ℕ) : ℕ := max M (max (M*3) (max (M*(5*M)) (M+1)))
```

## signedEnvelopeOrderBound

Source: `RequestProject\TypedTriangle\TowerPackingOrders.lean:12`.

```lean
def signedEnvelopeOrderBound (M : ℕ) : ℕ := max 2 (monitoredPackingOrderBound (packingSignedScale M))
```

## packingLocalizedScale

Source: `RequestProject\TypedTriangle\TowerPackingOrders.lean:13`.

```lean
def packingLocalizedScale (M : ℕ) : ℕ := max M (max (M*6) (max (6*M) (9*M)))
```

## localizedSignedOrderBound

Source: `RequestProject\TypedTriangle\TowerPackingOrders.lean:14`.

```lean
def localizedSignedOrderBound (M : ℕ) : ℕ := signedEnvelopeOrderBound (packingLocalizedScale M)
```

## packingPhysicalScale

Source: `RequestProject\TypedTriangle\TowerPackingOrders.lean:15`.

```lean
def packingPhysicalScale (M : ℕ) : ℕ := max M (max (2*M) (M*2))
```

## physicalMomentOrderBound

Source: `RequestProject\TypedTriangle\TowerPackingOrders.lean:16`.

```lean
def physicalMomentOrderBound (M : ℕ) : ℕ :=
  max (16*M+1) (localizedSignedOrderBound (packingPhysicalScale M))
```

## packingCoverRateBound

Source: `RequestProject\TypedTriangle\TowerPackingOrders.lean:19`.

```lean
def packingCoverRateBound (M : ℕ) : ℕ := max (M*64) (max (M*64) 64)
```

## packingCoverBudgetBound

Source: `RequestProject\TypedTriangle\TowerPackingOrders.lean:20`.

```lean
def packingCoverBudgetBound (M : ℕ) : ℕ := (packingCoverRateBound M)^2
```

## packingStockScale

Source: `RequestProject\TypedTriangle\TowerPackingOrders.lean:21`.

```lean
def packingStockScale (M : ℕ) : ℕ := max M (max (packingCoverBudgetBound M*4) 4)
```

## stockMomentOrderBound

Source: `RequestProject\TypedTriangle\TowerPackingOrders.lean:22`.

```lean
def stockMomentOrderBound (M : ℕ) : ℕ :=
  max (physicalMomentOrderBound (packingStockScale M))
    (max (packingCoverRateBound M) (2*packingCoverBudgetBound M))
```

## fixedPackingOrderBound

Source: `RequestProject\TypedTriangle\TowerPackingOrders.lean:25`.

```lean
def fixedPackingOrderBound (M : ℕ) : ℕ := stockMomentOrderBound M
```

## nativePartitionInputMajorant

Source: `RequestProject\TypedTriangle\TowerBankLayerOrders.lean:23`.

```lean
def nativePartitionInputMajorant (M : ℕ) : ℕ := M+2*M+paidDensityMajorant M+1
```

## nativePartitionOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankLayerOrders.lean:24`.

```lean
def nativePartitionOrderMajorant (M : ℕ) : ℕ :=
  max (layerComplementOrderMajorant M) (fixedPackingOrderBound (nativePartitionInputMajorant M))
```

## physicalGlueOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankWeights.lean:18`.

```lean
def physicalGlueOrderMajorant (M : ℕ) : ℕ :=
  max (max (compressionOrderMajorant M) (max (routeOrderMajorant M) (3*M+1))) (3*M+1)
```

## nativeWeightOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankWeights.lean:22`.

```lean
def nativeWeightOrderMajorant (M : ℕ) : ℕ := 4*physicalGlueOrderMajorant (2*M)*M+1
```

## bankOrderBound

Source: `RequestProject\TypedTriangle\TowerBankBudgets.lean:12`.

```lean
def bankOrderBound (M : ℕ) : ℕ := 8*(M*(M^2))+1
```

## bankStep

Source: `RequestProject\TypedTriangle\TowerBankLayerOrders.lean:115`.

```lean
def bankStep (M h : ℕ) : ℕ :=
  M+4096+128*M+64*M^2+4*M^3+(M+2)*M+
  catalogDimensionMajorant M+catalogCoefficientMajorant M+catalogColumnMajorant M+
  bankRadiusMajorant M+bankCatalogSizeMajorant M+bankCellSizeMajorant M h+
  bankProtectionBound M h+coreDeltaBound M h+deletionBudgetMajorant M+nativeDeleteMajorant M+
  natEnvelope 20 M+2*natEnvelope 4 M+bankToleranceBound M h+
  preparedBankRateMajorant M h M+physicalWeightMajorant M+bankEtaBound M M+monitorCapBound M M+
  resourceInputMajorant M+resourceOutputMajorant M+resourceCompletionMajorant M+
  stockBankOrderMajorant M h+nativePartitionOrderMajorant M+nativeWeightOrderMajorant M+bankOrderBound M
```

## bankStage

Source: `RequestProject\TypedTriangle\TowerBankLayerOrders.lean:161`.

```lean
def bankStage (h : ℕ) : ℕ → ℕ → ℕ
  | 0,M => M
  | k+1,M => bankStep (bankStage h k M) h
```

## layerThresholdMajorant

Source: `RequestProject\TypedTriangle\TowerBankLayerOrders.lean:165`.

```lean
def layerThresholdMajorant (M h : ℕ) : ℕ := bankStage h 16 M
```

## cleanLayerThresholdMajorant

Source: `RequestProject\TypedTriangle\TowerBankLayerOrders.lean:299`.

```lean
def cleanLayerThresholdMajorant (M h : ℕ) : ℕ :=
  max (layerThresholdMajorant (3*M+1) h) (2*max 1 M*M)
```

## windowRouteMajorant

Source: `RequestProject\TypedTriangle\TowerBankLayerBudgets.lean:18`.

```lean
def windowRouteMajorant (M : ℕ) : ℕ := M*M*(32*(M+1)*4^M)
```

## outerLayerParameterScale

Source: `RequestProject\TypedTriangle\TowerBankLayerBudgets.lean:19`.

```lean
def outerLayerParameterScale (M : ℕ) : ℕ :=
  M+M*16+2*M+M*32+M*4+windowRouteMajorant (2*M)*4+(M+1)+1
```

## scheduledPrecisionMajorant

Source: `RequestProject\TypedTriangle\TowerReferenceAgenda.lean:32`.

```lean
def scheduledPrecisionMajorant (M : ℕ) : ℕ := max (M*8) (128*M*M)
```

## scheduledOrderMajorant

Source: `RequestProject\TypedTriangle\TowerReferenceAgenda.lean:33`.

```lean
def scheduledOrderMajorant (M : ℕ) : ℕ := max 1 ((scheduledPrecisionMajorant M)^4)
```

## innerLayerOrderMajorant

Source: `RequestProject\TypedTriangle\TowerBankLayerOrders.lean:301`.

```lean
def innerLayerOrderMajorant (M h : ℕ) : ℕ :=
  max 1 (max (cleanLayerThresholdMajorant (outerLayerParameterScale M) h) (max (scheduledOrderMajorant M) (2*M)))
```

## thresholdLayerScale

Source: `RequestProject\TypedTriangle\TowerThresholdAssembly.lean:13`.

```lean
def thresholdLayerScale (A h : ℕ) : ℕ :=
  A+innerLayerOrderMajorant A h+max 1 (scheduledOrderMajorant A)+1
```

## rawPolynomialBound

Source: `RequestProject\TypedTriangle\TowerRawSample.lean:19`.

```lean
def rawPolynomialBound (R : ℕ) : ℕ := max 1 ((4*Nat.factorial 14)*R^14)
```

## rawHingeRateBound

Source: `RequestProject\TypedTriangle\TowerRawSample.lean:11`.

```lean
def rawHingeRateBound (M : ℕ) : ℕ :=
  (M^2 * M^(2*(M+2))) * ((4*(compressionPowerMajorant (M+6))^2)*(M+2))
```

## rawGeometryRateBound

Source: `RequestProject\TypedTriangle\TowerRawSample.lean:13`.

```lean
def rawGeometryRateBound (M : ℕ) : ℕ :=
  max (M^2*4) (max ((M^2*M^2)*4) (rawHingeRateBound M))
```

## rawTestRateBound

Source: `RequestProject\TypedTriangle\TowerRawSample.lean:17`.

```lean
def rawTestRateBound (M T : ℕ) : ℕ :=
  max (rawGeometryRateBound M) (max (M^2*(8*M)) T)
```

## rawAutomaticOrderBound

Source: `RequestProject\TypedTriangle\TowerRawSample.lean:20`.

```lean
def rawAutomaticOrderBound (M T : ℕ) : ℕ :=
  max 1 (max (rawPolynomialBound (rawTestRateBound M T)) 3)
```

## rawNativeTailBound

Source: `RequestProject\TypedTriangle\TowerRawSample.lean:15`.

```lean
def rawNativeTailBound (M : ℕ) : ℕ :=
  (nativeDensityMajorant M * M^(2*nativeInteriorMajorant M)) * (16*(nativeInteriorMajorant M)^2)
```

## oddPathOrderMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPaths.lean:14`.

```lean
def oddPathOrderMajorant (M : ℕ) : ℕ :=
  4*(oddPathMajorant M+2)^2*((M+1)^(oddPathMajorant M+3))+1
```

## nativeRouteOrderMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPaths.lean:57`.

```lean
def nativeRouteOrderMajorant (M : ℕ) : ℕ :=
  max (oddPathOrderMajorant (nativePathInputMajorant M)) (3*M+1)
```

## rawNativeSampleOrderBound

Source: `RequestProject\TypedTriangle\TowerRawSample.lean:22`.

```lean
def rawNativeSampleOrderBound (M : ℕ) : ℕ :=
  max (rawAutomaticOrderBound M (rawNativeTailBound M)) (max (nativeRouteOrderMajorant M) 1)
```

## rawGlobalInputBound

Source: `RequestProject\TypedTriangle\TowerRawOrders.lean:20`.

```lean
def rawGlobalInputBound (M : ℕ) : ℕ := max M (max (M*2) (2*M))
```

## globalRawStepOrderBound

Source: `RequestProject\TypedTriangle\TowerRawOrders.lean:21`.

```lean
def globalRawStepOrderBound (M : ℕ) : ℕ :=
  max (max (rawNativeSampleOrderBound (rawGlobalInputBound M)) ((8*(M+1))^4))
    (max (2*M*M) 1)
```

## nestedOrderMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryBudgets.lean:24`.

```lean
def nestedOrderMajorant (M : ℕ) : ℕ := (16+16*M*compressionPowerMajorant M)*M+1
```

## entryOrderMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:27`.

```lean
def entryOrderMajorant (M : ℕ) : ℕ := max (nestedOrderMajorant M) (2*compressionOrderMajorant (M*2))
```

## coreOrderMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:28`.

```lean
def coreOrderMajorant (M : ℕ) : ℕ := max (nestedOrderMajorant M) (2*M)
```

## preparationOrderMajorant

Source: `RequestProject\TypedTriangle\TowerGeometryPreparation.lean:29`.

```lean
def preparationOrderMajorant (M : ℕ) : ℕ :=
  max (entryOrderMajorant M) (2*max (entryOrderMajorant M) (coreOrderMajorant M))
```

## rawGeometryShapeBound

Source: `RequestProject\TypedTriangle\TowerRawOrders.lean:11`.

```lean
def rawGeometryShapeBound (M K A : ℕ) : ℕ :=
  max ((A*(M+1))^4) (max (32^4) (max (4*K) (((2*(M+1))*compressionPowerMajorant M)*K)))
```

## rawRequiredGeometryBound

Source: `RequestProject\TypedTriangle\TowerRawOrders.lean:13`.

```lean
def rawRequiredGeometryBound (M : ℕ) : ℕ := rawGeometryShapeBound M ((M*M^M)*4) 8
```

## rawMinimumOrderBound

Source: `RequestProject\TypedTriangle\TowerRawOrders.lean:15`.

```lean
def rawMinimumOrderBound (M : ℕ) : ℕ :=
  max (max (preparationOrderMajorant (M*4)) M) (max 1 (rawRequiredGeometryBound M+1))
```

## rawTerminalInputBound

Source: `RequestProject\TypedTriangle\TowerRawOrders.lean:24`.

```lean
def rawTerminalInputBound (M : ℕ) : ℕ := max M (2*rawMinimumOrderBound M)
```

## rawTerminalOrderBound

Source: `RequestProject\TypedTriangle\TowerRawOrders.lean:25`.

```lean
def rawTerminalOrderBound (M : ℕ) : ℕ :=
  max (globalRawStepOrderBound (rawTerminalInputBound M)) (rawMinimumOrderBound M)
```

## thresholdTerminalScale

Source: `RequestProject\TypedTriangle\TowerThresholdAssembly.lean:15`.

```lean
def thresholdTerminalScale (R : ℕ) : ℕ := R+rawTerminalOrderBound R+8*R+1
```

## placementDenBound

Source: `RequestProject\TypedTriangle\TowerNatTerminal.lean:10`.

```lean
def placementDenBound (M k s : ℕ) : ℕ := 2*(1+k+s+2*s*s*(M+1))
```

## terminalBudgetBound

Source: `RequestProject\TypedTriangle\TowerNatTerminal.lean:12`.

```lean
def terminalBudgetBound (M t s : ℕ) : ℕ := 2*(M*placementDenBound M t s)
```

## reserveBudgetBound

Source: `RequestProject\TypedTriangle\TowerNatTerminal.lean:128`.

```lean
def reserveBudgetBound (M K h t : ℕ) : ℕ :=
  terminalBudgetBound (supplyBudgetBound M h) t (supplySizeBound K h (t*t))
```

## reserveRateBound

Source: `RequestProject\TypedTriangle\TowerNatTerminal.lean:133`.

```lean
def reserveRateBound (M K h t : ℕ) : ℕ := max 64 (reserveBudgetBound M K h t*4)
```

## terminalUniformRateMajorant

Source: `RequestProject\TypedTriangle\TowerTerminalCaps.lean:25`.

```lean
def terminalUniformRateMajorant (M h : ℕ) : ℕ := reserveRateBound M (uniformCertMajorant M) h M
```

## placementOrderBound

Source: `RequestProject\TypedTriangle\TowerNatTerminal.lean:11`.

```lean
def placementOrderBound (M s : ℕ) : ℕ := 2*s*M+1
```

## terminalOrderBound

Source: `RequestProject\TypedTriangle\TowerNatTerminal.lean:13`.

```lean
def terminalOrderBound (M t s : ℕ) : ℕ :=
  placementOrderBound M s+2*(2^(t*t)+t)*(M*placementDenBound M t s)
```

## reserveOrderBound

Source: `RequestProject\TypedTriangle\TowerNatTerminal.lean:130`.

```lean
def reserveOrderBound (M K h t : ℕ) : ℕ :=
  max (supplyOrderBound M K h (t*t))
    (terminalOrderBound (supplyBudgetBound M h) t (supplySizeBound K h (t*t)))
```

## terminalUniformOrderMajorant

Source: `RequestProject\TypedTriangle\TowerTerminalCaps.lean:26`.

```lean
def terminalUniformOrderMajorant (M h : ℕ) : ℕ := reserveOrderBound M (uniformCertMajorant M) h M
```

## reserveSizeBound

Source: `RequestProject\TypedTriangle\TowerNatTerminal.lean:127`.

```lean
def reserveSizeBound (K h t : ℕ) : ℕ := supplySizeBound K h (t*t)*2^(t*t)
```

## terminalReserveSizeMajorant

Source: `RequestProject\TypedTriangle\TowerTerminalCaps.lean:27`.

```lean
def terminalReserveSizeMajorant (M h : ℕ) : ℕ := reserveSizeBound (uniformCertMajorant M) h M
```

## thresholdReserveScale

Source: `RequestProject\TypedTriangle\TowerThresholdAssembly.lean:16`.

```lean
def thresholdReserveScale (T h : ℕ) : ℕ :=
  T+terminalUniformRateMajorant T h+4*T+terminalUniformOrderMajorant T h+
    compressionOrderMajorant T+terminalReserveSizeMajorant T h+1
```

## outerRawRequiredGeometryBound

Source: `RequestProject\TypedTriangle\TowerRawOrders.lean:14`.

```lean
def outerRawRequiredGeometryBound (M : ℕ) : ℕ := rawGeometryShapeBound M (M*M^M) 4
```

## outerRawMinimumOrderBound

Source: `RequestProject\TypedTriangle\TowerRawOrders.lean:17`.

```lean
def outerRawMinimumOrderBound (M : ℕ) : ℕ :=
  max (max (preparationOrderMajorant (M*4)) M) (max 1 (outerRawRequiredGeometryBound M+1))
```

## outerRawAutoInputBound

Source: `RequestProject\TypedTriangle\TowerRawOrders.lean:27`.

```lean
def outerRawAutoInputBound (M : ℕ) : ℕ := max M (max (4*M) (2*M))
```

## outerRawRootOrderBound

Source: `RequestProject\TypedTriangle\TowerRawOrders.lean:28`.

```lean
def outerRawRootOrderBound (M T : ℕ) : ℕ :=
  let B := outerRawMinimumOrderBound M
  2*max (rawAutomaticOrderBound (outerRawAutoInputBound M) T) (max B (2*B*M))+2
```

## rawOuterTestRateBound

Source: `RequestProject\TypedTriangle\TowerRawSample.lean:24`.

```lean
def rawOuterTestRateBound (M : ℕ) : ℕ :=
  max (((M*2)^2*M^2)*16)
    (((nativeDensityMajorant M*2)*M^(2*nativeInteriorMajorant M)) * (16*(nativeInteriorMajorant M)^2))
```

## nativeOuterInputBound

Source: `RequestProject\TypedTriangle\TowerRawOrders.lean:31`.

```lean
def nativeOuterInputBound (M : ℕ) : ℕ := max M (8*M)
```

## nativeOuterRootOrderBound

Source: `RequestProject\TypedTriangle\TowerRawOrders.lean:32`.

```lean
def nativeOuterRootOrderBound (M : ℕ) : ℕ :=
  max (outerRawRootOrderBound M (rawOuterTestRateBound (nativeOuterInputBound M)))
    (nativeRouteOrderMajorant (nativeOuterInputBound M))
```

## rawRootOrderBound

Source: `RequestProject\TypedTriangle\TowerRawOrders.lean:19`.

```lean
def rawRootOrderBound (M : ℕ) : ℕ := 2*rawMinimumOrderBound M
```

## outerInnerInputBound

Source: `RequestProject\TypedTriangle\TowerRawOrders.lean:35`.

```lean
def outerInnerInputBound (M : ℕ) : ℕ := max M (max 16 (rawRootOrderBound M))
```

## outerInnerRootOrderBound

Source: `RequestProject\TypedTriangle\TowerRawOrders.lean:36`.

```lean
def outerInnerRootOrderBound (M : ℕ) : ℕ := nativeOuterRootOrderBound (outerInnerInputBound M)
```

## jointTrianglePackingOrderMajorant

Source: `RequestProject\TypedTriangle\TowerTrianglePacking.lean:11`.

```lean
def jointTrianglePackingOrderMajorant (M : ℕ) : ℕ := localizedSignedOrderBound (M+1)
```

## triangleStockInputMajorant

Source: `RequestProject\TypedTriangle\TowerTrianglePacking.lean:12`.

```lean
def triangleStockInputMajorant (M : ℕ) : ℕ := M+packingCoverBudgetBound M*4+4+1
```

## triangleStockOrderMajorant

Source: `RequestProject\TypedTriangle\TowerTrianglePacking.lean:13`.

```lean
def triangleStockOrderMajorant (M : ℕ) : ℕ :=
  max (jointTrianglePackingOrderMajorant (triangleStockInputMajorant M))
    (max (packingCoverRateBound M) (2*packingCoverBudgetBound M))
```

## triangleFixedPackingOrderMajorant

Source: `RequestProject\TypedTriangle\TowerTrianglePacking.lean:16`.

```lean
def triangleFixedPackingOrderMajorant (M : ℕ) : ℕ := triangleStockOrderMajorant M
```

## monitorFixedPartitionOrderMajorant

Source: `RequestProject\TypedTriangle\TowerTrianglePacking.lean:17`.

```lean
def monitorFixedPartitionOrderMajorant (M : ℕ) : ℕ :=
  max (triangleFixedPackingOrderMajorant (M+2)) 2
```

## triangleNativePartitionOrderMajorant

Source: `RequestProject\TypedTriangle\TowerTrianglePacking.lean:19`.

```lean
def triangleNativePartitionOrderMajorant (M : ℕ) : ℕ :=
  max (layerComplementOrderMajorant M)
    (max (monitorFixedPartitionOrderMajorant (nativePartitionInputMajorant M)) (max (16*M+1) 1))
```

## triangleBankStep

Source: `RequestProject\TypedTriangle\TowerTriangleLayerOrders.lean:44`.

```lean
def triangleBankStep (M h : ℕ) : ℕ :=
  bankStep M h + triangleNativePartitionOrderMajorant M + 1
```

## triangleBankStage

Source: `RequestProject\TypedTriangle\TowerTriangleLayerOrders.lean:83`.

```lean
def triangleBankStage (h : ℕ) : ℕ → ℕ → ℕ
  | 0,M => M
  | k+1,M => triangleBankStep (triangleBankStage h k M) h
```

## monitorLayerThresholdMajorant

Source: `RequestProject\TypedTriangle\TowerTriangleLayerOrders.lean:87`.

```lean
def monitorLayerThresholdMajorant (M h : ℕ) : ℕ := triangleBankStage h 16 M
```

## monitorCleanLayerThresholdMajorant

Source: `RequestProject\TypedTriangle\TowerTriangleLayerOrders.lean:223`.

```lean
def monitorCleanLayerThresholdMajorant (M h : ℕ) : ℕ :=
  max (monitorLayerThresholdMajorant (3*M+1) h) (2*max 1 M*M)
```

## monitorOuterLayerOrderMajorant

Source: `RequestProject\TypedTriangle\TowerTriangleLayerOrders.lean:225`.

```lean
def monitorOuterLayerOrderMajorant (M h : ℕ) : ℕ :=
  max 1 (max (monitorCleanLayerThresholdMajorant (outerLayerParameterScale M) h) (2*M))
```

## rawStockBudgetMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:196`.

```lean
def rawStockBudgetMajorant (M : ℕ) : ℕ := max (referenceStockBudgetBound M) (M*8)
```

## withdrawalStockMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:142`.

```lean
def withdrawalStockMajorant (M : ℕ) : ℕ :=
  max (forkEpsilonMajorant (withdrawalKappaMajorant M)) (selectorStockMajorant M*4)
```

## resourceTerminalMajorant

Source: `RequestProject\TypedTriangle\TowerBankResources.lean:197`.

```lean
def resourceTerminalMajorant (M : ℕ) : ℕ :=
  max (rawStockBudgetMajorant M) (max (withdrawalStockMajorant M) (M*M*16))
```

## layerTerminalInputMajorant

Source: `RequestProject\TypedTriangle\TowerBankLayerBudgets.lean:15`.

```lean
def layerTerminalInputMajorant (M : ℕ) : ℕ := M+2*M+2*bankProtectionBound M M+1
```

## layerTerminalMajorant

Source: `RequestProject\TypedTriangle\TowerBankLayerBudgets.lean:16`.

```lean
def layerTerminalMajorant (M : ℕ) : ℕ :=
  max (resourceTerminalMajorant (layerTerminalInputMajorant M)) ((M+1)*M*64)
```

## outerLayerTerminalMajorant

Source: `RequestProject\TypedTriangle\TowerBankLayerBudgets.lean:21`.

```lean
def outerLayerTerminalMajorant (M : ℕ) : ℕ := layerTerminalMajorant (outerLayerParameterScale M)
```

## triangleThresholdFinalMajorant

Source: `RequestProject\TypedTriangle\TowerTriangleThresholdAssembly.lean:13`.

```lean
def triangleThresholdFinalMajorant (U h : ℕ) : ℕ :=
  U+outerInnerRootOrderBound U+monitorOuterLayerOrderMajorant U h+U*outerLayerTerminalMajorant U+1
```

## paperIIITriangleTowerHeight

Source: `RequestProject\TypedTriangle\TowerTriangleThresholdAssembly.lean:18`.

```lean
def paperIIITriangleTowerHeight (K hOriginal qStat : ℕ) : ℕ :=
  let h := initialHingeOrder hOriginal
  let M := triangleThresholdInputMajorant K hOriginal qStat
  let A := thresholdAgendaMajorant M
  let R := thresholdLayerScale A h
  let T := thresholdTerminalScale R
  let U := thresholdReserveScale T h
  triangleThresholdFinalMajorant U h
```
