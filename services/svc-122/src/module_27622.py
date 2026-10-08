"""Service module 27622: business logic, no crypto."""


def calculate_total_27622(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27622():
    return 'module 27622 handles orders and invoices'
