"""Service module 29867: business logic, no crypto."""


def calculate_total_29867(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29867():
    return 'module 29867 handles orders and invoices'
