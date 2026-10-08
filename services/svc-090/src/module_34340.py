"""Service module 34340: business logic, no crypto."""


def calculate_total_34340(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34340():
    return 'module 34340 handles orders and invoices'
