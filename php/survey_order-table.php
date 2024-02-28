<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('survey_orders', function (Blueprint $table) {
            $table->id();
            //$table->foreignId('branch_id')->constrained('branches')->cascadeOnUpdate()->restrictOnDelete();
            $table->string('order_no');
            $table->string('order_status');
            $table->foreignId('customer_id')->constrained()->cascadeOnUpdate()->cascadeOnDelete();
            $table->string('address');
            $table->foreignId('township_id')->constrained()->cascadeOnUpdate()->cascadeOnDelete();
            //$table->date('order_date');
            $table->foreignId('survey_service_id')->constrained()->cascadeOnUpdate()->cascadeOnDelete();
            $table->foreignId('deep_cleaning_service_id')->constrained()->cascadeOnUpdate()->cascadeOnDelete();
            //$table->string('remark')->nullable()->default(null);
            $table->time('survey_date');
            $table->time('survey_time');
            $table->foreignId('surveyor_id')->constrained('labours')->cascadeOnUpdate()->restrictOnDelete();
            //$table->enum('order_status', config('enums.order_status'))->nullable()->default(null);
            //$table->string('cancel_reason')->nullable()->default(null);
            $table->float('area')->nullable()->default(null);
            $table->string('area_unit')->nullable()->default(null);
            $table->integer('total_labour')->default(0);
            $table->integer('total_working_day')->default(0);
            $table->integer('total_service_charges')->default(0);
            //$table->integer('survey_charges')->default(0);
            //$table->string('image_file_name')->nullable()->default(null);
            $table->string('deep_cleaning_order')->nullable()->default(null); //yes, no , not_sure
            $table->foreignId('created_uid')->nullable()->default(null)->constrained('users')->cascadeOnUpdate()->onDelete('no action');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('survey_orders');
    }
};