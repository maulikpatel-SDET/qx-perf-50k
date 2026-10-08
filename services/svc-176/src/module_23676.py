"""Service module 23676: business logic, no crypto."""


def calculate_total_23676(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23676():
    return 'module 23676 handles orders and invoices'
