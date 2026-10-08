"""Service module 28314: business logic, no crypto."""


def calculate_total_28314(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28314():
    return 'module 28314 handles orders and invoices'
