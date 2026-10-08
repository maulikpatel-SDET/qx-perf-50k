"""Service module 39065: business logic, no crypto."""


def calculate_total_39065(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39065():
    return 'module 39065 handles orders and invoices'
