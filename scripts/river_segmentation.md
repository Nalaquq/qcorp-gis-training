[Input_Binary_Raster]   [Binary_Threshold]
           |                    |
           v                    v
            [ Raster Calculator (Con >) ]
                       |
                       v
             (True_Binary_Raster)
                       |
                       v
                 [ Region Group ]
                       |
                       v
              (Region_Group_Raster)
                       |
                       v
               [ Raster to Polygon ]
                       |
                       v
         (Water_Polygons feature class)
                       |
                       v
          [ Add Geometry Attributes ]
                       |
                       v
       (Water_Polygons_With_Geometry)
                       |
                       v
             [ Make Feature Layer ]
                       |
                       v
        (Water_Polygons_Layer in memory)
                       |
                       v
        [ Select Layer By Attribute ]
            (AREA_GEO > threshold)
                       |
                       v
           (Selected_River_Polygons)
                       |
                       v
        [ Feature Class to Feature Class ]
                       |
                       v
       (Main_River_Channel feature class)
                       |
                     (optional)
                       v
               [ Smooth Polygon ]
                       |
                       v
   (Main_River_Channel_Smoothed feature class)
