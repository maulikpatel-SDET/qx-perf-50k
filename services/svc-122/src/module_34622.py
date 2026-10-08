"""Service module 34622: business logic, no crypto."""


def calculate_total_34622(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34622():
    return 'module 34622 handles orders and invoices'
