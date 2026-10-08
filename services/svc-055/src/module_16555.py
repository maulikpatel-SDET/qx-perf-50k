"""Service module 16555: business logic, no crypto."""


def calculate_total_16555(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16555():
    return 'module 16555 handles orders and invoices'
