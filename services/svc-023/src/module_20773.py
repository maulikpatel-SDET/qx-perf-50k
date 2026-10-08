"""Service module 20773: business logic, no crypto."""


def calculate_total_20773(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20773():
    return 'module 20773 handles orders and invoices'
