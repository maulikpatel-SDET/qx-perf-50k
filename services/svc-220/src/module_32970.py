"""Service module 32970: business logic, no crypto."""


def calculate_total_32970(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32970():
    return 'module 32970 handles orders and invoices'
