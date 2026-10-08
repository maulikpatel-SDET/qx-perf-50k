"""Service module 8809: business logic, no crypto."""


def calculate_total_8809(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8809():
    return 'module 8809 handles orders and invoices'
