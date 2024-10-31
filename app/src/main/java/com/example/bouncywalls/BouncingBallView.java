// bouncy-walls/app/src/main/java/com/example/bouncywalls/BouncingBallView.java
package com.example.bouncywalls;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.util.AttributeSet;
import android.view.MotionEvent;
import android.view.View;

public class BouncingBallView extends View {
    private Paint paint;
    private float ballX, ballY;
    private float ballRadius = 50;
    private float velocityX = 10, velocityY = 10;
    private boolean dragging = false;

    public BouncingBallView(Context context, AttributeSet attrs) {
        super(context, attrs);
        paint = new Paint();
        paint.setColor(Color.RED);
    }

    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        canvas.drawColor(Color.WHITE);
        canvas.drawCircle(ballX, ballY, ballRadius, paint);
        if (!dragging) {
            updateBallPosition();
        }
        invalidate();
    }

    private void updateBallPosition() {
        ballX += velocityX;
        ballY += velocityY;

        if (ballX - ballRadius < 0 || ballX + ballRadius > getWidth()) {
            velocityX = -velocityX;
        }
        if (ballY - ballRadius < 0 || ballY + ballRadius > getHeight()) {
            velocityY = -velocityY;
        }
    }

    @Override
    public boolean onTouchEvent(MotionEvent event) {
        switch (event.getAction()) {
            case MotionEvent.ACTION_DOWN:
                if (isTouchingBall(event.getX(), event.getY())) {
                    dragging = true;
                    return true;
                }
                break;
            case MotionEvent.ACTION_MOVE:
                if (dragging) {
                    ballX = event.getX();
                    ballY = event.getY();
                    invalidate();
                    return true;
                }
                break;
            case MotionEvent.ACTION_UP:
                dragging = false;
                break;
        }
        return super.onTouchEvent(event);
    }

    private boolean isTouchingBall(float x, float y) {
        float dx = x - ballX;
        float dy = y - ballY;
        return dx * dx + dy * dy <= ballRadius * ballRadius;
    }
}