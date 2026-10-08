"""Service module 676: business logic, no crypto."""


def calculate_total_676(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_676():
    return 'module 676 handles orders and invoices'
