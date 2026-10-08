"""Service module 31132: business logic, no crypto."""


def calculate_total_31132(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31132():
    return 'module 31132 handles orders and invoices'
