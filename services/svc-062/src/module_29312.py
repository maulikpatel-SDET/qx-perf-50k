"""Service module 29312: business logic, no crypto."""


def calculate_total_29312(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29312():
    return 'module 29312 handles orders and invoices'
