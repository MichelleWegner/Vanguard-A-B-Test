# metrics.py

def calculate_completion_rate(df, column='process_step'):
    """Calculate the completion rate based on the specified column."""
    completed = df[df[column] == 'confirm'].shape[0]
    total = df.shape[0]
    return completed / total

def calculate_error_rate(df, column='process_step'):
    """Calculate the error rate based on the specified column."""
    errors = df[df[column] != 'confirm'].shape[0]
    total = df.shape[0]
    return errors / total
