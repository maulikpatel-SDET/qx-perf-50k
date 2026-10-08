"""Service module 29368: business logic, no crypto."""


def calculate_total_29368(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29368():
    return 'module 29368 handles orders and invoices'
