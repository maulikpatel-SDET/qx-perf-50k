"""Service module 27868: business logic, no crypto."""


def calculate_total_27868(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27868():
    return 'module 27868 handles orders and invoices'
