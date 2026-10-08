"""Service module 32103: business logic, no crypto."""


def calculate_total_32103(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32103():
    return 'module 32103 handles orders and invoices'
