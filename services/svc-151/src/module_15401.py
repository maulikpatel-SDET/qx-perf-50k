"""Service module 15401: business logic, no crypto."""


def calculate_total_15401(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15401():
    return 'module 15401 handles orders and invoices'
