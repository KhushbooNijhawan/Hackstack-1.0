package com.example.Dormir;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;

public class Dashboard extends AppCompatActivity {
    ImageButton speed,connectMap;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);
        speed  = (ImageButton) findViewById(R.id.speed);
        connectMap  = (ImageButton) findViewById(R.id.connectMap);
        speed.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                speed();
            }
        });
        connectMap.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                connectMap1();
            }
        });
    }
    public void speed(){
        Intent intent = new Intent(this, SpeedActivity.class);
        startActivity(intent);
    }
    public void connectMap1(){
        Intent intent = new Intent(this, MapActivity.class);
        startActivity(intent);
    }
}
